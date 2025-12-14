
from django.urls import path
from . import views


app_name = 'apps.articulos'

urlpatterns = [
    path('Listar/', views.Listar_Articulos, name='path_listar_articulo'),
    path('Detalle<int:pk>/', views.Detalle_Articulo_Clase.as_view(), name='path_detalle_articulo'),
    path('Crear/', views.Crear_Articulo.as_view(), name='path_crear_articulo'),
    path('Modificar/<int:pk>',views.Modificar_Articulo.as_view(),name='path_modificar_articulo'),
    path('Eliminar/<int:pk>',views.Eliminar_Articulo.as_view(),name = 'path_eliminar_articulo'),

    # frases
    path('Frases/', views.frases, name='path_frases'),
    path('Frases/borrar/<int:frase_id>/', views.borrar_frase, name="path_borrar_frase"),


# CATEGORIAS
    path("Filtrar/<int:pk>", views.Filtrar_Categoria, name="path_filtro_categorias"),
]

