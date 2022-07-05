from django.shortcuts import render

def pagina_clientes(request):
    return render(request, 'clientes/pagina_clientes.html')

def matheus(request):
    return render(request, 'clientes/matheus.html')