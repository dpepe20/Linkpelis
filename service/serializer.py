from rest_framework import serializers
from pelis.models import *

class descarga_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Descarga
		fields = ('url','des_Nombre','link','fotejes','descripcion')


class estreno_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Extreno
		fields = ('url','ext_Nombree','ext_Idioma','ext_descripcion','fecha_estreno','imagenes')

class pelicula_serializer(serializers.ModelSerializer):

	
	class Meta:
		model = Pelicula
		fields =('url','nombre','descripcion','fecha','idioma','calidad','generos','filtros','descargas','imagen','Ver_online')

class genero_serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model  = Genero
		fields = '__all__'

class filtro_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Filtro
		fields = '__all__'

class recomendacion_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Recomendacion
		fields = '__all__'