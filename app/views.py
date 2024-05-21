from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def signin(request):
    return render(request, 'authentication/signin.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

def overview(request):
    return render(request, 'overview.html')

def newplanning(request):
    return render(request, 'new_planning.html')