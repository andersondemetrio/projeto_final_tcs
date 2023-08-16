document.addEventListener('DOMContentLoaded', function () {
    fetch("{% url 'cargos_vieww' %}")
        .then(response => response.json())
        .then(data => {
            const selectElement = document.querySelector('select[name="cargo"]');
            data.cargos.forEach(cargo => {
                const option = document.createElement('option');
                option.value = cargo.id;
                option.textContent = cargo.nome_cargo;
                selectElement.appendChild(option);
            });
        });
});

// seleciona o cargo do funcionário
