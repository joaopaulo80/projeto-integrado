let carrinho = [];
let total = 0;

function entrar(){

    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("senha").value;

    if(usuario && senha){

        document.getElementById("login").style.display = "none";
        document.getElementById("site").style.display = "block";

    }else{
        alert("Preencha todos os campos!");
    }
}

function adicionarCarrinho(nome,preco){

    carrinho.push({nome,preco});

    total += preco;

    atualizarCarrinho();
}

function atualizarCarrinho(){

    let lista = document.getElementById("itensCarrinho");

    lista.innerHTML = "";

    carrinho.forEach(item => {

        let li = document.createElement("li");

        li.innerHTML = `
            ${item.nome} - R$ ${item.preco}
        `;

        lista.appendChild(li);
    });

    document.getElementById("total").innerText = total;

    document.getElementById("contador").innerText = carrinho.length;
}

function abrirCarrinho(){
    document.getElementById("carrinho").classList.add("ativo");
}

function fecharCarrinho(){
    document.getElementById("carrinho").classList.remove("ativo");
}

function finalizarPedido(){

    if(carrinho.length == 0){

        alert("Carrinho vazio!");

        return;
    }

    document.getElementById("pagamento").style.display = "flex";
}

function pagar(){

    let metodo = document.getElementById("metodo").value;

    alert(`
Pedido realizado com sucesso!

Pagamento: ${metodo}

Total: R$ ${total}
    `);

    carrinho = [];
    total = 0;

    atualizarCarrinho();

    document.getElementById("pagamento").style.display = "none";

    fecharCarrinho();
}