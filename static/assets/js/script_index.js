document.addEventListener('DOMContentLoaded', function () {

    // Requisição Fetch para cargos
    fetch(cargosUrl)
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

    // Requisição Fetch para endereços
    fetch(enderecoUrl)
        .then(response => response.json())
        .then(data => {
            const selectElements = document.querySelectorAll('select[name="endereco"]');
            selectElements.forEach(selectElement => {
                data.enderecos.forEach(endereco => {
                    const option = document.createElement('option');
                    option.value = endereco.id;
                    option.textContent = endereco.endereco;
                    selectElement.appendChild(option);
                });
            });
        });


    // script para adicionar mais campos de despesas fixas

    document.getElementById('maisDespesasFixas').addEventListener('click', function () {
        const despesaContainer = document.querySelector('.despesa-container');
        const clone = despesaContainer.cloneNode(true);
        const descricaoInput = clone.querySelector('input[name="descricao"]');
        const valorInput = clone.querySelector('input[name="valor"]');
        descricaoInput.value = '';
        valorInput.value = '';
        despesaContainer.parentNode.insertBefore(clone, despesaContainer.nextSibling);
    });

    // scritp para adicionar mais campos de mão de obra
    document.getElementById('maisMaoDeObra').addEventListener('click', function () {
        const maoDeObraContainer = document.querySelector('.mao-de-obra-container');
        const clone = maoDeObraContainer.cloneNode(true);
        const matriculaInput = clone.querySelector('input[name="matricula"]');
        const nomeInput = clone.querySelector('input[name="nome"]');
        const cpfInput = clone.querySelector('input[name="cpf"]');
        const salarioInput = clone.querySelector('input[name="salario"]');
        const beneficiosInput = clone.querySelector('input[name="beneficios"]');
        const encargosInput = clone.querySelector('input[name="encargos"]');
        matriculaInput.value = '';
        nomeInput.value = '';
        cpfInput.value = '';
        salarioInput.value = '';
        beneficiosInput.value = '';
        encargosInput.value = '';
        maoDeObraContainer.parentNode.insertBefore(clone, maoDeObraContainer.nextSibling);
    });

    // Alerta da empresas cadastrada, ainda não funcionando
    const urlParams = new URLSearchParams(window.location.search);
    const success = urlParams.get('success');

    if (success === 'true') {
        alert('Empresa cadastrada com sucesso!');
    }

    // Validação do número da empresa
    document.addEventListener('DOMContentLoaded', function () {
        const numeroEmpresaInput = document.querySelector('input[name="numero_empresa"]');

        numeroEmpresaInput.addEventListener('input', function () {
            const maxDigits = 4;
            if (this.value.length > maxDigits) {
                alert(`Digite no máximo ${maxDigits} dígitos.`);
                this.value = this.value.slice(0, maxDigits);
            }
        });
    });

    // Ative todos os checkboxes de switch na página
    document.addEventListener('DOMContentLoaded', function () {
        var switchCheckboxes = document.querySelectorAll('.form-switch input[type="checkbox"]');
        switchCheckboxes.forEach(function (checkbox) {
            new bootstrap.Switch(checkbox);
        });
    });

});


// Importar a biblioteca jQuery (certifique-se de incluir isso no seu HTML)
// <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

// script_index.js (ou o arquivo onde está seu código JavaScript)

// Função para buscar e preencher os campos do endereço a partir do CEP
// Comentado por que não funcionou
// $(document).ready(function() {
//     // Capturando o evento de clique no botão de buscar CEP
//     $("#btnBuscarCEP").click(function() {
//         // Capturando o valor do campo de entrada do CEP
//         var cep = $("#cepInput").val();
        
//         // Construindo a URL da API ViaCEP com o CEP inserido
//         var url = "https://viacep.com.br/ws/" + cep + "/json/";
        
//         // Fazendo a requisição AJAX para a API ViaCEP
//         $.get(url, function(data) {
//             // Preenchendo os campos do formulário com os dados retornados pela API
//             $("#logradouro").val(data.logradouro);
//             $("#endereco").val(data.endereco);
//             $("#bairro").val(data.bairro);
//             $("#cidade").val(data.localidade);
//             $("#estado").val(data.uf);
//         });
//     });
// });

