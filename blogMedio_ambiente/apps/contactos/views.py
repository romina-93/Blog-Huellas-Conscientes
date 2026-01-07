from django.shortcuts import render

from .forms import ContactoForm

def contacto_view(request):
    mensaje_exito = None  # Variable para mostrar mensaje si todo sale bien

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje_exito = "¡Mensaje enviado con éxito! Gracias por contactarnos."
            form = ContactoForm()  # Reinicia el formulario vacío
    else:
        form = ContactoForm()

    return render(request, "contactos/contactos.html", {
        "form": form,
        "mensaje_exito": mensaje_exito
    })
