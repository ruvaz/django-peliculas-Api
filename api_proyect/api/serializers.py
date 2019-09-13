from .models import Pelicula
from rest_framework import serializers


#definiciones del model serilizer, indica como debe serializar para formato json las peliculas
class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
