from django.urls import path
from app.views import index, imagem, signin, overview, newplanning

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('login', signin, name='signin'),
    path('overview', overview, name='overview'),
    path('new-planning', newplanning, name='new-planning')
]
