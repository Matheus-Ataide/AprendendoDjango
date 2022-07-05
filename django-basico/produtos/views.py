from django.shortcuts import render

def pagina_produtos(request):
    return render(request, 'produtos/pagina_produtos.html')

def celulares(request):
    return render(request, 'produtos/celulares.html')