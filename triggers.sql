-- =========================
-- Триггеры для основных таблиц
-- =========================

-- ===== Пример: Логирование удаления из таблицы si =====

CREATE TABLE IF NOT EXISTS si_delete_log (
    id SERIAL PRIMARY KEY,
    si_id INTEGER,
    deleted_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION trg_log_si_delete() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO si_delete_log (si_id) VALUES (OLD."id_SI");
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER si_after_delete
AFTER DELETE ON si
FOR EACH ROW EXECUTE FUNCTION trg_log_si_delete();

-- ===== Пример: Запрет удаления si, если есть связанные сертификаты =====

CREATE OR REPLACE FUNCTION trg_prevent_si_delete_if_certificates() RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE si_id = OLD."id_SI") THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить СИ, для которого существуют сертификаты!';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER si_before_delete
BEFORE DELETE ON si
FOR EACH ROW EXECUTE FUNCTION trg_prevent_si_delete_if_certificates();

-- ===== Логирование удаления из таблицы employees =====

CREATE TABLE IF NOT EXISTS employees_delete_log (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER,
    deleted_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION trg_log_employee_delete() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO employees_delete_log (employee_id) VALUES (OLD.id_employee);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER employees_after_delete
AFTER DELETE ON employees
FOR EACH ROW EXECUTE FUNCTION trg_log_employee_delete();

-- ===== Пример: Автоматическое обновление даты изменения сертификата =====

ALTER TABLE certificates_certificate
    ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP;

CREATE OR REPLACE FUNCTION trg_update_certificates_certificate_timestamp() RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER certificates_certificate_before_update
BEFORE UPDATE ON certificates_certificate
FOR EACH ROW EXECUTE FUNCTION trg_update_certificates_certificate_timestamp();

-- ===== Пример: Логирование удаления эталона (references) =====

CREATE TABLE IF NOT EXISTS references_delete_log (
    id SERIAL PRIMARY KEY,
    reference_id INTEGER,
    deleted_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION trg_log_reference_delete() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO references_delete_log (reference_id) VALUES (OLD.id_reference);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER references_after_delete
AFTER DELETE ON "references"
FOR EACH ROW EXECUTE FUNCTION trg_log_reference_delete();

-- ===== Пример: Запрет удаления verification_types, если есть связанные сертификаты =====

CREATE OR REPLACE FUNCTION trg_prevent_verification_type_delete_if_certificates() RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE verification_type_id = OLD.id_verification_type) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить тип поверки, для которого существуют сертификаты!';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER verification_types_before_delete
BEFORE DELETE ON verification_types
FOR EACH ROW EXECUTE FUNCTION trg_prevent_verification_type_delete_if_certificates();

-- ===== Пример: Логирование удаления из si_types =====

CREATE TABLE IF NOT EXISTS si_types_delete_log (
    id SERIAL PRIMARY KEY,
    si_type_id INTEGER,
    deleted_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION trg_log_si_type_delete() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO si_types_delete_log (si_type_id) VALUES (OLD."id_SI_type");
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER si_types_after_delete
AFTER DELETE ON si_types
FOR EACH ROW EXECUTE FUNCTION trg_log_si_type_delete();

-- ===== Пример: Запрет удаления эталона, если он используется в сертификатах =====

CREATE OR REPLACE FUNCTION trg_prevent_reference_delete_if_certificates() RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE affecting_factors_id = OLD.id_reference) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить эталон, который используется в сертификатах!';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER references_before_delete
BEFORE DELETE ON "references"
FOR EACH ROW EXECUTE FUNCTION trg_prevent_reference_delete_if_certificates();

-- ===== Пример: Логирование удаления сертификата =====

CREATE TABLE IF NOT EXISTS certificates_certificate_delete_log (
    id SERIAL PRIMARY KEY,
    certificate_id INTEGER,
    deleted_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION trg_log_certificate_delete() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO certificates_certificate_delete_log (certificate_id) VALUES (OLD.id);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER certificates_certificate_after_delete
AFTER DELETE ON certificates_certificate
FOR EACH ROW EXECUTE FUNCTION trg_log_certificate_delete();

-- ===== certificates_certificate: Проверка существования связанных записей при вставке (BEFORE INSERT) =====
CREATE OR REPLACE FUNCTION trg_check_certificates_certificate_fk() RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM si WHERE "id_SI" = NEW.si_id) THEN
        RAISE EXCEPTION 'Ошибка: СИ с id % не существует', NEW.si_id;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM verification_types WHERE id_verification_type = NEW.verification_type_id) THEN
        RAISE EXCEPTION 'Ошибка: Тип поверки с id % не существует', NEW.verification_type_id;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM employees WHERE id_employee = NEW.verifier_id) THEN
        RAISE EXCEPTION 'Ошибка: Сотрудник с id % не существует', NEW.verifier_id;
    END IF;
    IF NEW.affecting_factors_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM affecting_factors WHERE id_affecting_factors = NEW.affecting_factors_id) THEN
        RAISE EXCEPTION 'Ошибка: Влияющий фактор с id % не существует', NEW.affecting_factors_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER certificates_certificate_before_insert
BEFORE INSERT ON certificates_certificate
FOR EACH ROW EXECUTE FUNCTION trg_check_certificates_certificate_fk();

-- ===== employees: Запрет удаления, если есть связанные сертификаты (BEFORE DELETE) =====
CREATE OR REPLACE FUNCTION trg_prevent_employee_delete_if_certificates() RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE verifier_id = OLD.id_employee) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить сотрудника, который указан в сертификатах!';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER employees_before_delete
BEFORE DELETE ON employees
FOR EACH ROW EXECUTE FUNCTION trg_prevent_employee_delete_if_certificates();

-- =========================
-- Конец triggers.sql
-- =========================