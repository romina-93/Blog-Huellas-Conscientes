from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario
from apps.articulos.models import Articulo
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

def Comentar(request, pk):
	con = Articulo.objects.get(pk = pk)
	usuario = request.user
	com = request.POST.get('comentario',None)

	Comentario.objects.create(texto=com, contenido=con, usuario=usuario)

	return HttpResponseRedirect(reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':pk}))

class Eliminar(DeleteView):
	model = Comentario
	def get_success_url(self):
		return reverse_lazy('articulos:path_detalle_articulo', kwargs={'pk':self.object.articulo.pk})