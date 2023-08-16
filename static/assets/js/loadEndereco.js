document.addEventListener('DOMContentLoaded', function () {
    const enderecoUrl = document.getElementById('modalCadastros').getAttribute('data-endereco-url');

    fetch(enderecoUrl)
        .then(response => response.json())
        .then(data => {
            const selectElement = document.querySelector('select[name="endereco"]');
            data.enderecos.forEach(endereco => {
                const option = document.createElement('option');
                option.value = endereco.id;
                option.textContent = endereco.endereco;
                selectElement.appendChild(option);
            });
        });
});
