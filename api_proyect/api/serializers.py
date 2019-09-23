from .models import Pelicula
from rest_framework import serializers
from .models import Pelicula, PeliculaFavorita

# definiciones del model serilizer, indica como debe serializar para formato json las peliculas


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'


class PeliculaFavoritaSerializer(serializers.ModelSerializer):
    #serializa los mismos campos que en pelicula
    pelicula = PeliculaSerializer()

    class Meta:
        #modelo a usar
        model = PeliculaFavorita
        #serialize el campo pelicula con el serializador de arriba
        fields = ['pelicula']
