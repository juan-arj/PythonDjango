from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {'titulo': 'Apex Eletronics | Home'}
    return render(request, 'home/index.html', contexto)