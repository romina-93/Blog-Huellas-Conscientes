from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario


class RegistroUsuario(CreateView):
    template_name = 'usuarios/login.html'  
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuarios:path_login')

    def form_invalid(self, form):
        """
        Si el formulario de registro tiene errores,
        volvemos a cargar el login pero con el form_registro lleno
        y abriendo el modal automáticamente.
        """
        return render(self.request, "usuarios/login.html", {
            "form_registro": form,
            "abrir_modal": True
        })
