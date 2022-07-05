from django.urls import path, include
from inicio.views import index

urlpatterns = [
    path("", index),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),

]
