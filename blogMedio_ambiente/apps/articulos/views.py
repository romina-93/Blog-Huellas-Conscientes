
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from apps.articulos.models import Articulo, FraseInspiradora
import unicodedata

from django.http import HttpResponseForbidden

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import FormularioCrearArticulo, FormularioModificarArticulo

from apps.categorias.models import Categoria

from .models import Articulo

from .models import FraseInspiradora
from .forms import FraseForm

#DECORADOR PARA UNA VBF QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.decorators import login_required

#MIXINS PARA UNA VBC QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin

#Decorador para una VBF para controlar si el usuario es staff
from django.contrib.admin.views.decorators import staff_member_required

#MIXIN PARAUNA VBC PARA CONTROLAR EL TIPO DE USUARIO (lo usamos para ver si es staff)
from django.contrib.auth.mixins import UserPassesTestMixin

# Normalizar texto (quita acentos y pasa a minúsculas)

def normalizar(texto):
    if not texto:
        return ""
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn')


def Inicio(request):
    query = request.GET.get("q", "").strip()

    # Filtros individuales
    categoria_id = request.GET.get("categoria", "")
    orden = request.GET.get("orden", "")
    alf = request.GET.get("alf", "")

    # Detectar qué está activo
    hay_filtros = bool(categoria_id or orden or alf)
    hay_buscador = bool(query)  

    # --------- INICIO LIMPIO ----------#
    if not hay_filtros and not hay_buscador:
        articulos = Articulo.objects.all().order_by('-fecha')
        articulos_recientes = articulos[:4]
        articulos_relevantes = Articulo.objects.filter(destacado=True)[:4]

        frases = FraseInspiradora.objects.all().order_by('-id')

        return render(request, "inicio.html", {
            "inicio_limpio": True,
            "articulos": articulos,
            "categorias": Categoria.objects.all(),
            "articulos_recientes": articulos_recientes,
            "articulos_relevantes": articulos_relevantes,

            # filtros vacíos
            "f_categoria": "",
            "f_orden": "",
            "f_alf": "",
            "query": "",
            "frases": frases,
        })

    # --------- BUSCADOR ----------
    if hay_buscador:
        query_norm = normalizar(query)
        todos = Articulo.objects.all()
        resultados = []

        for articulo in todos:
            titulo_norm = normalizar(articulo.titulo)
            contenido_norm = normalizar(articulo.contenido)
            categoria_norm = normalizar(articulo.categoria.nombre)

            if (query_norm in titulo_norm or
                query_norm in contenido_norm or
                query_norm in categoria_norm):
                resultados.append(articulo)

        articulos = resultados
        resultados = resultados
    else:
        resultados = None
        articulos = Articulo.objects.all()

    # --------- FILTROS ----------
    if categoria_id:
        articulos = articulos.filter(categoria_id=categoria_id)

    if orden == "asc":
        articulos = articulos.order_by("fecha")
    elif orden == "desc":
        articulos = articulos.order_by("-fecha")

    if alf == "asc":
        articulos = articulos.order_by("titulo")
    elif alf == "desc":
        articulos = articulos.order_by("-titulo")

    # --------- BARRA LATERAL ----------
    articulos_recientes = Articulo.objects.all().order_by('-fecha')[:4]
    articulos_relevantes = Articulo.objects.filter(destacado=True).order_by('-fecha')[:4]


    frases = FraseInspiradora.objects.all().order_by('-id')  # las más nuevas primero

    return render(request, "inicio.html", {
        "inicio_limpio": False,
        "articulos": articulos,
        "resultados": resultados,
        "categorias": Categoria.objects.all(),
        "query": query,
        "f_categoria": categoria_id,
        "f_orden": orden,
        "f_alf": alf,
        "articulos_recientes": articulos_recientes,
        "articulos_relevantes": articulos_relevantes,
        "frases": frases
    })

# VISTA BASADA EN FUNCIONES
#@login_required
#@staff_member_required
def Listar_Articulos(request):
    valor_a_ordenar = request.GET.get('orden', None)

    if valor_a_ordenar == 'asc':
          recientes = Articulo.objects.all().order_by('fecha')
    elif valor_a_ordenar == 'desc':
          recientes = Articulo.objects.all().order_by('-fecha')
    else:
         recientes = Articulo.objects.all().order_by('-fecha')  # por defecto

    categoria_bd = Categoria.objects.all()

    return render(
        request,
        'articulos/listar.html',
        {'articulos': recientes, 'categorias': categoria_bd})

#VBC
class Detalle_Articulo_Clase(DetailView):
    template_name = "articulos/detalle.html"
    model = Articulo
    context_object_name = 'articulo'

class Crear_Articulo(LoginRequiredMixin,UserPassesTestMixin,CreateView):
	model = Articulo
	template_name = 'articulos/crear.html'
	form_class = FormularioCrearArticulo
	success_url = reverse_lazy('articulos:path_listar_articulo')
	def test_func(self):
		if self.request.user.is_staff:
			return True
		else:
			return False

class Modificar_Articulo(UpdateView):
	model = Articulo
	template_name = 'articulos/modificar.html'
	form_class = FormularioModificarArticulo
	success_url = reverse_lazy('articulos:path_listar_articulo')

class Eliminar_Articulo(DeleteView):
	model = Articulo
	success_url = reverse_lazy('articulos:path_listar_articulo')
      
	#articulos_filtrados = Categoria.objects.filter(categoria=categoria_filtrado)
      
def Filtrar_Categoria(request, pk):
    categoria_filtrado = Categoria.objects.get(pk = pk)
    articulos_filtrados = Articulo.objects.filter(categoria=categoria_filtrado)
    return render(request, "articulos/filtrados.html", {"articulos": articulos_filtrados,
													 "nombre_categoria": categoria_filtrado.nombre})



@login_required(login_url=reverse_lazy('usuarios:path_login'))
def frases(request):
    frases = FraseInspiradora.objects.all()
    form = FraseForm()

    if request.method == 'POST':
        form = FraseForm(request.POST)
        if form.is_valid():
            nueva_frase = form.save(commit=False)
            nueva_frase.usuario = request.user   # ← AGREGA EL USUARIO
            nueva_frase.save()
            return redirect('path_inicio')

    return render(request, 'articulos/frases.html', {
        'frases': frases,
        'form': form,
    })


@login_required
def borrar_frase(request, frase_id):
    frase = get_object_or_404(FraseInspiradora, id=frase_id)

    # Solo el autor o un admin pueden borrar
    if request.user != frase.usuario and not request.user.is_superuser:
        return HttpResponseForbidden("No tenés permiso para borrar esta frase.")

    if request.method == "POST":
        frase.delete()
        return redirect('path_inicio')

    return render(request, "articulos/frases_confirm_delete.html", {
        "frase": frase
    })
