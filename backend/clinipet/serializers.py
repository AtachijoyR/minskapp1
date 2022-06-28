from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    """Esta es la clase PetSerializar, su función es transformar los datos del modelo Pet a formato json para su futura llamada desde
    el frontend

    Args:
         serializers.ModelSerializer: serializador que tomará la forma del modelo Pet
    """
    class Meta:
        model = Pet
        fields =('__all__') 


        