from django.shortcuts import render

# Create your views here.
def contato(request):
    contexto = {'titulo': 'Apex Eletronics | Contato'}
    return render(request, 'contato/index.html', contexto)