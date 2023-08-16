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


//  Insere mais campos na mão de obra