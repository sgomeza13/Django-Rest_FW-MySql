from rest_framework import serializers
from .models import Nombre

class NombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nombre
        fields = '__all__'