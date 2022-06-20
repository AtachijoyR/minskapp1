from django.shortcuts import render

from .models import Pet
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveUpdateAPIView)
from rest_framework import status

from .serializers import PetSerializer
# Create your views here.


#clase que permite listar las mascotas
class ListPets(ListAPIView):
    serializer_class = PetSerializer
    def get_queryset(self):
        return Pet.objects.all()


class FiltrarPets(ListAPIView):
    #Se escoge el serializador que entrega los datos de todas las mascotas
    serializer_class = PetSerializer

    #función para filtrar en base a un identificador (en este caso rut del dueño)
    def get_queryset(self):
        rutOwner = self.kwargs['owner']
        lista = Pet.objects.filter(
            rut_owner = rutOwner
        )
        return lista

#Clase para Crear Mascotas Requerimiento 2
class CrearPets(CreateAPIView):
    serializer_class = PetSerializer

#Clase para Crear Mascotas Requerimiento
class UpdatePet(RetrieveUpdateAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

