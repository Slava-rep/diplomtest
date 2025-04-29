// static/js/certificate_form.js
document.addEventListener('DOMContentLoaded', function() {
    // Автодополнение для СИ
    $('.select2').select2({
        ajax: {
            url: $(this).data('url'),
            dataType: 'json',
            delay: 250,
            processResults: function(data) {
                return {
                    results: data.map(item => ({
                        id: item.id,
                        text: `${item.registration_number} - ${item.type__name}`
                    }))
                };
            }
        }
    });
    
    // Расчет даты окончания
    $('#id_verification_date, #id_interval').on('change', function() {
        const start = new Date($('#id_verification_date').val());
        const years = parseInt($('#id_interval').val()) || 1;
        start.setFullYear(start.getFullYear() + years);
        $('#id_next_verification_date').val(start.toISOString().split('T')[0]);
    });

    const typeSelect = document.getElementById('id_verification_type');
    const methodSelect = document.getElementById('id_verification_method');

    if (typeSelect && methodSelect) {
        typeSelect.addEventListener('change', function() {
            const typeId = this.value;
            fetch(`/api/verification-methods/?type_id=${typeId}`)
                .then(response => response.json())
                .then(data => {
                    methodSelect.innerHTML = data.map(m => 
                        `<option value="${m.id}">${m.name}</option>`
                    ).join('');
                });
        });
    }

});