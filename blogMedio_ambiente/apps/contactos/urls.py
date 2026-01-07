from django.urls import path
from . import views

# INDICO COMO SE LLAMA LA APP
app_name= "apps.contactos"

urlpatterns = [
    path('Contactos/', views.contacto_view, name = 'path_contacto'),
]