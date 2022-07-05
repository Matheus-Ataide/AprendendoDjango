from django.shortcuts import render

def pagina_produtos(request):
    return render(request, 'produtos/pagina_produtos.html')

def celulares(request):
    return render(request, 'produtos/celulares.html')

    context = {
        'nome' : 'Matheus',
        'ultimo acesso' : data_atual(),
        'idade': 18,
        'produtos': [
            {'nome' : 'Leptop Dell', 'preco' : '1.200,00'},
            {'nome' : 'Iphone', 'preco' : '6.400,00'},
            {'nome' : 'Samsung', 'preco' : '2.100,00'},
        ]
    }
