from django.urls import path
from app.views import index, imagem, signin

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('login', signin, name='signin')
]
