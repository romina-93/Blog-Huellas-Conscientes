from django.shortcuts import render, get_object_or_404
from .models import Categoria

def Listar_Categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias.html', {'categorias': categorias})

def Detalle_Categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    articulos = categoria.articulos.all()
    return render(request, 'categorias/detalle.html', {
        'categoria': categoria,
        'articulos': articulos,
    })
