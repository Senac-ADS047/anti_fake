document.querySelector("form").addEventListener("submit", function(e) {
    e.preventDefault();

    const senha = document.getElementById("senha").value;
    const confirmar = document.getElementById("confirmar").value;

    if (senha !== confirmar) {
        alert("As senhas não coincidem!");
    } else {
        alert("Cadastro realizado com sucesso!");
    }
});