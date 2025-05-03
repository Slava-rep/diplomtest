-- =========================
-- Хранимые процедуры для основных таблиц
-- =========================

-- ===== Таблица: si =====

-- Добавление записи
CREATE OR REPLACE FUNCTION si_insert(
    p_registration_number VARCHAR,
    p_year_of_manufacture INTEGER,
    p_modification VARCHAR,
    p_serial_number VARCHAR,
    p_si_type_id INTEGER
) RETURNS INTEGER AS $$
DECLARE
    new_id INTEGER;
BEGIN
    INSERT INTO si (registration_number, year_of_manufacture, modification, serial_number, si_type_id)
    VALUES (p_registration_number, p_year_of_manufacture, p_modification, p_serial_number, p_si_type_id)
    RETURNING "id_SI" INTO new_id;
    RETURN new_id;
END;
$$ LANGUAGE plpgsql;

-- Обновление записи
CREATE OR REPLACE FUNCTION si_update(
    p_id INTEGER,
    p_registration_number VARCHAR,
    p_year_of_manufacture INTEGER,
    p_modification VARCHAR,
    p_serial_number VARCHAR,
    p_si_type_id INTEGER
) RETURNS VOID AS $$
BEGIN
    UPDATE si
    SET registration_number = p_registration_number,
        year_of_manufacture = p_year_of_manufacture,
        modification = p_modification,
        serial_number = p_serial_number,
        si_type_id = p_si_type_id
    WHERE "id_SI" = p_id;
END;
$$ LANGUAGE plpgsql;

-- Удаление записи с проверкой наличия связанных сертификатов
CREATE OR REPLACE FUNCTION si_delete(p_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE si_id = p_id) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить СИ, для которого существуют сертификаты!';
    END IF;
    DELETE FROM si WHERE "id_SI" = p_id;
END;
$$ LANGUAGE plpgsql;

-- ===== Таблица: si_types =====

CREATE OR REPLACE FUNCTION si_types_insert(
    p_gov_registry_number VARCHAR,
    p_si_name VARCHAR,
    p_type_designation VARCHAR,
    p_manufacturer VARCHAR,
    p_record_number VARCHAR,
    p_publication_date DATE,
    p_description_document TEXT,
    p_calibration_method_document TEXT,
    p_procedure VARCHAR,
    p_certificate_term DATE,
    p_periodic_calibration BOOLEAN,
    p_serial_number VARCHAR,
    p_status VARCHAR,
    p_verification_method_id INTEGER
) RETURNS INTEGER AS $$
DECLARE
    new_id INTEGER;
BEGIN
    INSERT INTO si_types (
        gov_registry_number, si_name, type_designation, manufacturer, record_number,
        publication_date, description_document, calibration_method_document, procedure,
        certificate_term, periodic_calibration, serial_number, status, verification_method_id
    )
    VALUES (
        p_gov_registry_number, p_si_name, p_type_designation, p_manufacturer, p_record_number,
        p_publication_date, p_description_document, p_calibration_method_document, p_procedure,
        p_certificate_term, p_periodic_calibration, p_serial_number, p_status, p_verification_method_id
    )
    RETURNING "id_SI_type" INTO new_id;
    RETURN new_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION si_types_update(
    p_id INTEGER,
    p_gov_registry_number VARCHAR,
    p_si_name VARCHAR,
    p_type_designation VARCHAR,
    p_manufacturer VARCHAR,
    p_record_number VARCHAR,
    p_publication_date DATE,
    p_description_document TEXT,
    p_calibration_method_document TEXT,
    p_procedure VARCHAR,
    p_certificate_term DATE,
    p_periodic_calibration BOOLEAN,
    p_serial_number VARCHAR,
    p_status VARCHAR,
    p_verification_method_id INTEGER
) RETURNS VOID AS $$
BEGIN
    UPDATE si_types
    SET gov_registry_number = p_gov_registry_number,
        si_name = p_si_name,
        type_designation = p_type_designation,
        manufacturer = p_manufacturer,
        record_number = p_record_number,
        publication_date = p_publication_date,
        description_document = p_description_document,
        calibration_method_document = p_calibration_method_document,
        procedure = p_procedure,
        certificate_term = p_certificate_term,
        periodic_calibration = p_periodic_calibration,
        serial_number = p_serial_number,
        status = p_status,
        verification_method_id = p_verification_method_id
    WHERE "id_SI_type" = p_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION si_types_delete(p_id INTEGER) RETURNS VOID AS $$
BEGIN
    DELETE FROM si_types WHERE "id_SI_type" = p_id;
END;
$$ LANGUAGE plpgsql;

-- ===== Таблица: verification_types =====

CREATE OR REPLACE FUNCTION verification_types_insert(
    p_name VARCHAR
) RETURNS INTEGER AS $$
DECLARE
    new_id INTEGER;
BEGIN
    INSERT INTO verification_types (name)
    VALUES (p_name)
    RETURNING id_verification_type INTO new_id;
    RETURN new_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION verification_types_update(
    p_id INTEGER,
    p_name VARCHAR
) RETURNS VOID AS $$
BEGIN
    UPDATE verification_types
    SET name = p_name
    WHERE id_verification_type = p_id;
END;
$$ LANGUAGE plpgsql;

-- Удаление с проверкой наличия связанных сертификатов
CREATE OR REPLACE FUNCTION verification_types_delete(p_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE verification_type_id = p_id) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить тип поверки, для которого существуют сертификаты!';
    END IF;
    DELETE FROM verification_types WHERE id_verification_type = p_id;
END;
$$ LANGUAGE plpgsql;

-- ===== Таблица: certificates_certificate =====

-- Вставка с проверкой существования связанных записей
CREATE OR REPLACE FUNCTION certificates_certificate_insert(
    p_gov_reg_number VARCHAR,
    p_inventory_number VARCHAR,
    p_modification VARCHAR,
    p_status VARCHAR,
    p_created_at TIMESTAMP,
    p_number VARCHAR,
    p_verification_date DATE,
    p_interval INTEGER,
    p_next_verification_date DATE,
    p_verification_result VARCHAR,
    p_previous_verification_mark VARCHAR,
    p_is_vn BOOLEAN,
    p_mark_in_passport BOOLEAN,
    p_mark_on_si BOOLEAN,
    p_organization_name VARCHAR,
    p_inn VARCHAR,
    p_department_head VARCHAR,
    p_composition TEXT,
    p_comment TEXT,
    p_protocol VARCHAR,
    p_affecting_factors_id INTEGER,
    p_si_id INTEGER,
    p_verification_method_id INTEGER,
    p_verification_type_id INTEGER,
    p_verifier_id INTEGER
) RETURNS INTEGER AS $$
DECLARE
    new_id INTEGER;
BEGIN
    -- Проверка существования связанных записей
    IF NOT EXISTS (SELECT 1 FROM si WHERE "id_SI" = p_si_id) THEN
        RAISE EXCEPTION 'Ошибка: СИ с id % не существует', p_si_id;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM verification_types WHERE id_verification_type = p_verification_type_id) THEN
        RAISE EXCEPTION 'Ошибка: Тип поверки с id % не существует', p_verification_type_id;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM employees WHERE id_employee = p_verifier_id) THEN
        RAISE EXCEPTION 'Ошибка: Сотрудник с id % не существует', p_verifier_id;
    END IF;
    IF p_affecting_factors_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM affecting_factors WHERE id_affecting_factors = p_affecting_factors_id) THEN
        RAISE EXCEPTION 'Ошибка: Влияющий фактор с id % не существует', p_affecting_factors_id;
    END IF;
    -- Вставка
    INSERT INTO certificates_certificate (
        gov_reg_number, inventory_number, modification, status, created_at, "number",
        verification_date, "interval", next_verification_date, verification_result,
        previous_verification_mark, is_vn, mark_in_passport, mark_on_si, organization_name,
        inn, department_head, composition, comment, protocol, affecting_factors_id,
        si_id, verification_method_id, verification_type_id, verifier_id
    )
    VALUES (
        p_gov_reg_number, p_inventory_number, p_modification, p_status, p_created_at, p_number,
        p_verification_date, p_interval, p_next_verification_date, p_verification_result,
        p_previous_verification_mark, p_is_vn, p_mark_in_passport, p_mark_on_si, p_organization_name,
        p_inn, p_department_head, p_composition, p_comment, p_protocol, p_affecting_factors_id,
        p_si_id, p_verification_method_id, p_verification_type_id, p_verifier_id
    )
    RETURNING id INTO new_id;
    RETURN new_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION certificates_certificate_update(
    p_id INTEGER,
    p_gov_reg_number VARCHAR,
    p_inventory_number VARCHAR,
    p_modification VARCHAR,
    p_status VARCHAR,
    p_created_at TIMESTAMP,
    p_number VARCHAR,
    p_verification_date DATE,
    p_interval INTEGER,
    p_next_verification_date DATE,
    p_verification_result VARCHAR,
    p_previous_verification_mark VARCHAR,
    p_is_vn BOOLEAN,
    p_mark_in_passport BOOLEAN,
    p_mark_on_si BOOLEAN,
    p_organization_name VARCHAR,
    p_inn VARCHAR,
    p_department_head VARCHAR,
    p_composition TEXT,
    p_comment TEXT,
    p_protocol VARCHAR,
    p_affecting_factors_id INTEGER,
    p_si_id INTEGER,
    p_verification_method_id INTEGER,
    p_verification_type_id INTEGER,
    p_verifier_id INTEGER
) RETURNS VOID AS $$
BEGIN
    UPDATE certificates_certificate
    SET gov_reg_number = p_gov_reg_number,
        inventory_number = p_inventory_number,
        modification = p_modification,
        status = p_status,
        created_at = p_created_at,
        "number" = p_number,
        verification_date = p_verification_date,
        "interval" = p_interval,
        next_verification_date = p_next_verification_date,
        verification_result = p_verification_result,
        previous_verification_mark = p_previous_verification_mark,
        is_vn = p_is_vn,
        mark_in_passport = p_mark_in_passport,
        mark_on_si = p_mark_on_si,
        organization_name = p_organization_name,
        inn = p_inn,
        department_head = p_department_head,
        composition = p_composition,
        comment = p_comment,
        protocol = p_protocol,
        affecting_factors_id = p_affecting_factors_id,
        si_id = p_si_id,
        verification_method_id = p_verification_method_id,
        verification_type_id = p_verification_type_id,
        verifier_id = p_verifier_id
    WHERE id = p_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION certificates_certificate_delete(p_id INTEGER) RETURNS VOID AS $$
BEGIN
    DELETE FROM certificates_certificate WHERE id = p_id;
END;
$$ LANGUAGE plpgsql;

-- ===== Таблица: employees =====

CREATE OR REPLACE FUNCTION employees_insert(
    p_full_name VARCHAR,
    p_birth_date DATE,
    p_birth_place VARCHAR,
    p_snils VARCHAR,
    p_email VARCHAR,
    p_work_contract VARCHAR,
    p_specialization VARCHAR,
    p_qualification VARCHAR,
    p_diploma VARCHAR,
    p_diploma_year INTEGER,
    p_practical_experience INTEGER,
    p_note TEXT
) RETURNS INTEGER AS $$
DECLARE
    new_id INTEGER;
BEGIN
    INSERT INTO employees (
        full_name, birth_date, birth_place, snils, email, work_contract,
        specialization, qualification, diploma, diploma_year, practical_experience, note
    )
    VALUES (
        p_full_name, p_birth_date, p_birth_place, p_snils, p_email, p_work_contract,
        p_specialization, p_qualification, p_diploma, p_diploma_year, p_practical_experience, p_note
    )
    RETURNING id_employee INTO new_id;
    RETURN new_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION employees_update(
    p_id INTEGER,
    p_full_name VARCHAR,
    p_birth_date DATE,
    p_birth_place VARCHAR,
    p_snils VARCHAR,
    p_email VARCHAR,
    p_work_contract VARCHAR,
    p_specialization VARCHAR,
    p_qualification VARCHAR,
    p_diploma VARCHAR,
    p_diploma_year INTEGER,
    p_practical_experience INTEGER,
    p_note TEXT
) RETURNS VOID AS $$
BEGIN
    UPDATE employees
    SET full_name = p_full_name,
        birth_date = p_birth_date,
        birth_place = p_birth_place,
        snils = p_snils,
        email = p_email,
        work_contract = p_work_contract,
        specialization = p_specialization,
        qualification = p_qualification,
        diploma = p_diploma,
        diploma_year = p_diploma_year,
        practical_experience = p_practical_experience,
        note = p_note
    WHERE id_employee = p_id;
END;
$$ LANGUAGE plpgsql;

-- Удаление с проверкой наличия связанных сертификатов
CREATE OR REPLACE FUNCTION employees_delete(p_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE verifier_id = p_id) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить сотрудника, который указан в сертификатах!';
    END IF;
    DELETE FROM employees WHERE id_employee = p_id;
END;
$$ LANGUAGE plpgsql;

-- ===== Таблица: references =====

CREATE OR REPLACE FUNCTION references_insert(
    p_range VARCHAR,
    p_standard_type VARCHAR,
    p_brand VARCHAR,
    p_fif_registration_number VARCHAR,
    p_country_of_manufacturer VARCHAR,
    p_manufacturer_name VARCHAR,
    p_manufacture_year INTEGER,
    p_commissioning_year INTEGER,
    p_inventory_number VARCHAR,
    p_serial_number VARCHAR,
    p_measurement_range VARCHAR,
    p_uncertainty VARCHAR,
    p_calibration_results_link VARCHAR,
    p_calibration_certificate_date DATE,
    p_calibration_certificate_validity DATE,
    p_calibration_certificate_number VARCHAR,
    p_ownership VARCHAR,
    p_installation_location VARCHAR,
    p_note TEXT,
    p_name VARCHAR,
    p_description TEXT,
    p_factory_number VARCHAR
) RETURNS INTEGER AS $$
DECLARE
    new_id INTEGER;
BEGIN
    INSERT INTO "references" (
        range, standard_type, brand, fif_registration_number, country_of_manufacturer,
        manufacturer_name, manufacture_year, commissioning_year, inventory_number, serial_number,
        measurement_range, uncertainty, calibration_results_link, calibration_certificate_date,
        calibration_certificate_validity, calibration_certificate_number, ownership,
        installation_location, note, name, description, factory_number
    )
    VALUES (
        p_range, p_standard_type, p_brand, p_fif_registration_number, p_country_of_manufacturer,
        p_manufacturer_name, p_manufacture_year, p_commissioning_year, p_inventory_number, p_serial_number,
        p_measurement_range, p_uncertainty, p_calibration_results_link, p_calibration_certificate_date,
        p_calibration_certificate_validity, p_calibration_certificate_number, p_ownership,
        p_installation_location, p_note, p_name, p_description, p_factory_number
    )
    RETURNING id_reference INTO new_id;
    RETURN new_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION references_update(
    p_id INTEGER,
    p_range VARCHAR,
    p_standard_type VARCHAR,
    p_brand VARCHAR,
    p_fif_registration_number VARCHAR,
    p_country_of_manufacturer VARCHAR,
    p_manufacturer_name VARCHAR,
    p_manufacture_year INTEGER,
    p_commissioning_year INTEGER,
    p_inventory_number VARCHAR,
    p_serial_number VARCHAR,
    p_measurement_range VARCHAR,
    p_uncertainty VARCHAR,
    p_calibration_results_link VARCHAR,
    p_calibration_certificate_date DATE,
    p_calibration_certificate_validity DATE,
    p_calibration_certificate_number VARCHAR,
    p_ownership VARCHAR,
    p_installation_location VARCHAR,
    p_note TEXT,
    p_name VARCHAR,
    p_description TEXT,
    p_factory_number VARCHAR
) RETURNS VOID AS $$
BEGIN
    UPDATE "references"
    SET range = p_range,
        standard_type = p_standard_type,
        brand = p_brand,
        fif_registration_number = p_fif_registration_number,
        country_of_manufacturer = p_country_of_manufacturer,
        manufacturer_name = p_manufacturer_name,
        manufacture_year = p_manufacture_year,
        commissioning_year = p_commissioning_year,
        inventory_number = p_inventory_number,
        serial_number = p_serial_number,
        measurement_range = p_measurement_range,
        uncertainty = p_uncertainty,
        calibration_results_link = p_calibration_results_link,
        calibration_certificate_date = p_calibration_certificate_date,
        calibration_certificate_validity = p_calibration_certificate_validity,
        calibration_certificate_number = p_calibration_certificate_number,
        ownership = p_ownership,
        installation_location = p_installation_location,
        note = p_note,
        name = p_name,
        description = p_description,
        factory_number = p_factory_number
    WHERE id_reference = p_id;
END;
$$ LANGUAGE plpgsql;

-- Удаление с проверкой наличия связанных сертификатов
CREATE OR REPLACE FUNCTION references_delete(p_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM certificates_certificate WHERE affecting_factors_id = p_id) THEN
        RAISE EXCEPTION 'Ошибка: Нельзя удалить эталон, который используется в сертификатах!';
    END IF;
    DELETE FROM "references" WHERE id_reference = p_id;
END;
$$ LANGUAGE plpgsql;
