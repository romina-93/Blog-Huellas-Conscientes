
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings 
from django.urls import path, include
from apps.articulos.views import Inicio 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , Inicio, name = 'path_inicio'),
    

    #enlazar a la url de las app
    path('Categorias/', include(('apps.categorias.urls', 'categorias'), namespace='categorias')),
    path('Articulos/', include(('apps.articulos.urls', 'articulos'), namespace='articulos')),
    path('Contactos/', include(('apps.contactos.urls', 'contactos'), namespace='contactos')),
    path('Comentarios/', include(('apps.comentarios.urls', 'comentarios'), namespace='comentarios')),
    path('Usuarios/', include(('apps.usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('Nosotros/', include(('apps.nosotros.urls', 'nosotros'), namespace='nosotros')),
	path('Sector-chaco/', views.sector_chaco, name='sector_chaco'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
