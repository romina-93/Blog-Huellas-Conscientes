from django.urls import path
from . import views

# INDICO COMO SE LLAMA LA APP
app_name= "apps.nosotros"

urlpatterns = [
    path('Nosotros', views.sobre_nosotros, name = 'path_nosotros'),
]