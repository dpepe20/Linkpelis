from django.shortcuts import render
from pelis.models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.



class descarga_views(viewsets.ModelViewSet):
	queryset = Descarga.objects.all()
	serializer_class = descarga_serializer

class estreno_views(viewsets.ModelViewSet):
	queryset = Extreno.objects.all()
	serializer_class = estreno_serializer

class pelicula_views(viewsets.ModelViewSet):
	queryset = Pelicula.objects.all()
	serializer_class = pelicula_serializer

class genero_views(viewsets.ModelViewSet):
	queryset = Genero.objects.all()
	serializer_class = genero_serializer

class filtro_views(viewsets.ModelViewSet):
	queryset  = Filtro.objects.all()
	serializer_class = filtro_serializer

class recomendacion_views(viewsets.ModelViewSet):
	queryset = Recomendacion.objects.all()
	serializer_class = recomendacion_serializer