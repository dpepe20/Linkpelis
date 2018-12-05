from django.urls import path, include
from rest_framework import routers
from pelis.models import *
from service.views import *



router = routers.DefaultRouter()
router.register(r'Descarga',descarga_views)
router.register(r'Extreno',estreno_views)
router.register(r'Pelicula',pelicula_views)
router.register(r'Genero',genero_views)
router.register(r'Filtro',filtro_views)
router.register(r'Recomendacion',recomendacion_views)



urlpatterns =	[
	path('api/',include(router.urls)),
	path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]