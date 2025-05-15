<div id="alerta"></div>
        function verificarDados() {
            var cartao = document.getElementById("numero").value;
            var cvv = document.getElementById("cvv").value;


            if (cartao === "" || cvv === "") {
                document.getElementById("alerta").innerHTML =
                    '<div class="alert alert-warning" role="alert">Por favor, preencha todos os campos!</div>';
            } else/*(user === "admin" && pass === "12345")*/ {
                document.getElementById("alerta").innerHTML =
                    '<div class="alert alert-success" role="alert">Pedido realizado com sucesso!</div>';
                   // window.location.href = "index.html"; // Redireciona para a página index.html
            } 
        }


        function limparCampos() {
        document.getElementById("alerta").innerHTML = ""; // Limpa o conteúdo da div
    }      
