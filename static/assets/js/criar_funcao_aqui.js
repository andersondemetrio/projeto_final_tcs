// criar_funcao_aqui.js

function validarFormulario() {
    // Obter os valores dos campos de usuário e senha
    var usuario = document.getElementById("usuario").value;
    var senha = document.getElementById("senha").value;

    // Validar se os campos estão preenchidos
    if (usuario === "" || senha === "") {
        alert("Por favor, preencha todos os campos!");
        return false; // Impede o envio do formulário
    }

    // Adicione aqui suas regras de validação personalizadas, se necessário

    // Se chegou até aqui, os campos estão preenchidos corretamente
    return true; // Permite o envio do formulário
}

// função para esconder ou revelar senha da tela de login

document.addEventListener("DOMContentLoaded", function () {
    var togglePassword = document.getElementById("toggle-password");
    var passwordField = document.getElementById("password");

    togglePassword.addEventListener("click", function () {
        if (passwordField.type === "password") {
            passwordField.type = "text";
            togglePassword.classList.remove("fa-eye-slash");
            togglePassword.classList.add("fa-eye");
        } else {
            passwordField.type = "password";
            togglePassword.classList.remove("fa-eye");
            togglePassword.classList.add("fa-eye-slash");
        }
    });
});

// função para verificar erros na redefinição de senhas
document.addEventListener('DOMContentLoaded', function() {
    const password1Input = document.querySelector('#id_new_password1');
    const password2Input = document.querySelector('#id_new_password2');
    const password1Error = document.querySelector('#password1Error');
    const password2Error = document.querySelector('#password2Error');

    password1Input.addEventListener('input', () => {
        const password = password1Input.value;

        if (password.length < 8) {
            password1Error.textContent = 'A senha deve ter pelo menos 8 caracteres.';
        } else if (!/\d/.test(password) || !/[a-zA-Z]/.test(password)) {
            password1Error.textContent = 'A senha deve conter letras e números.';
        } else {
            password1Error.textContent = ''; // Remover a mensagem de erro
        }
    });

    password2Input.addEventListener('input', () => {
        if (password2Input.value !== password1Input.value) {
            password2Error.textContent = 'As senhas não coincidem.';
        } else {
            password2Error.textContent = ''; // Remover a mensagem de erro
        }
    });
});


