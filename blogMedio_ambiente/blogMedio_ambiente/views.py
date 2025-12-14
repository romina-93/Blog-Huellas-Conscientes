from django.shortcuts import render
from apps.articulos.models import Articulo
from apps.categorias.models import Categoria


def Inicio(request):
    articulos_recientes = Articulo.objects.all().order_by('-fecha')[:5]
    articulos_relevantes = Articulo.objects.filter(destacado=True).order_by('-fecha')[:5]

    # todas las categorías
    categorias = Categoria.objects.all()

    # armar lista con categoría + sus articulos
    categorias_con_articulos = []
    for cat in categorias:
        categorias_con_articulos.append({
            "categoria": cat,
            "articulos": Articulo.objects.filter(categoria=cat).order_by('-fecha')[:3]
        })

    return render(request, "inicio.html", {
        "articulos_recientes": articulos_recientes,
        "articulos_relevantes": articulos_relevantes,
        "categorias_con_articulos": categorias_con_articulos,
    })


def sector_chaco(request):
    return render(request, 'sector_chaco.html')
