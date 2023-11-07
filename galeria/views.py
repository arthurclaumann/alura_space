from django.shortcuts import render
from galeria.models import Fotografia

def index(request):

    # Iremos enviar o dicionário dados para o index html através da função render, mas para passarmos os dados para o software, ao invés de criarmos uma variável com os dados, iremos acessar os dados da base de dados

    # dados = {
    # 1: {"nome":"Nebulosa de Carina",
    #     'legenda': 'webbtelescope.org / NASA / James Webb'},
    # 2: {'nome': 'Galaxia NCG 1079',
    #     'legenda': 'nasa.org / NASA / Hubble'}
    # }
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request):
    return render(request, 'galeria/imagem.html')