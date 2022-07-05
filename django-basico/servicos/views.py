from django.shortcuts import render

def pagina_servicos(request):
    return render(request, 'servicos/pagina_servicos.html')

def limpeza(request):
    return render(request, 'servicos/limpeza.html')