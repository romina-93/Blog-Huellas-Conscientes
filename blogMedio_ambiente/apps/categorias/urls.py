
from django.urls import path
from . import views

app_name = 'apps.categorias'

urlpatterns = [
    path('Categorias', views.Listar_Categorias, name='path_listar_categoria'),
    path('Detalle/', views.Detalle_Categoria, name='path_detalle_categoria'),
]
