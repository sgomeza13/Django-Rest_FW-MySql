from rest_framework import viewsets
from .models import Nombre
from .serialiazer import NombreSerializer

# Create your views here.
class NombreViewSet(viewsets.ModelViewSet):
    queryset = Nombre.objects.all()
    serializer_class = NombreSerializer