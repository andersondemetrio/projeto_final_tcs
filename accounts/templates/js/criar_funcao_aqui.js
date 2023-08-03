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
  