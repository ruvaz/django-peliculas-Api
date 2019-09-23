from .models import Pelicula, PeliculaFavorita
from .serializers import PeliculaSerializer, PeliculaFavoritaSerializer

from django.shortcuts import get_object_or_404

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import viewsets, views, filters


class PeliculaViewSet(viewsets.ModelViewSet):
    # obtenemos peliculas
    queryset = Pelicula.objects.all()
    # las manda a serializar con el formato indicado en serilizer
    serializer_class = PeliculaSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo']
    ordering_fields = ['favoritos']


class MarcarPeliculaFavorita(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# POST -> Se usa para crear un recurso sin un identificador
  # PUT -> Se usa para crear/reemplazar un recurso con un identificador

def post(self, request):
    # obtenemos la pelicula o da 0, lo que daria error
    pelicula = get_object_or_404(Pelicula, id=self.request.data.get('id', 0))

    # obtener la relacion entre usuario y pelicula, la creara si no se encuentra
    favorita, created = PeliculaFavorita.objects.get_or_create(
        pelicula=pelicula, usuario=request.user)

    # Por defecto suponemos que se crea bien, diccionario en formato json
    content = {
        'id': pelicula.id,
        'favorita': True
    }

    # Si no se ha creado es que ya existe, entonces borramos el favorito
    if not created:
        favorita.delete()
        content['favorita'] = False

    # respuesta en formato json
    return Response(content)


class ListarPeliculasFavoritas(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET -> Se usa para hacer lecturas

    def get(self, request):

        peliculas_favoritas = PeliculaFavorita.objects.filter(
            usuario=request.user)
        serializer = PeliculaFavoritaSerializer(
            peliculas_favoritas, many=True)

        return Response(serializer.data)
