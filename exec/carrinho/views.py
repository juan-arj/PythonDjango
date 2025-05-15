from django.shortcuts import render
from carrinho.models import Compra

# Create your views here.
def carrinho(request):
    contexto = {'titulo': 'Apex Eletronics | Carrinho',
    'compras': Compra.objects.all(),
    }

    return render(request, 'carrinho/index.html', contexto)

def gravarCompra(request):
    nova_compra = Compra()
    nova_compra.nome = request.POST.get("nome")
    nova_compra.email = request.POST.get("email")
    nova_compra.endereco = request.POST.get("endereco")
    nova_compra.cidade = request.POST.get("cidade")
    nova_compra.cep = request.POST.get("cep")
    nova_compra.num_cartao = request.POST.get("numero")
    nova_compra.nome_cartao = request.POST.get("cartao")
    nova_compra.validade = request.POST.get("validade")
    nova_compra.cvv = request.POST.get("cvv")
    nova_compra.save()
    
    return carrinho(request)