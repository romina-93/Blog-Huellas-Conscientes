
# Create your views here.
from django.shortcuts import render

def sobre_nosotros(request):
    return render(request, "nosotros/sobre_nosotros.html")
