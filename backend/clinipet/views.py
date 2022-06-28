from django.shortcuts import render

from .models import Pet
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveUpdateAPIView)
from rest_framework import generics
from rest_framework import status

from .serializers import PetSerializer
# Create your views here.


#clase que permite listar las mascotas

class ListPets(ListAPIView):
    """ Esta es la clase ListPets

    Args:
        ListAPIView (_type_): Proporciona un control de metodo Get se utiliza para endpoints de solo lectura

    """
    serializer_class = PetSerializer
    def get_queryset(self):
        """Esta es una funcion que Accede al modelo Pet y posteriormente retorna todos los objetos del modelo mismo.
        Returns:
            Pet.objects.all(): Pet es modelo asociado al archivo models de clinipet el cual permite almacenar datos
            de las mascotas. la llamada a objects.all() se utiliza para retornar todos los objetos pertencientes a
            un conjunto de datos.
        """
        return Pet.objects.all()



class FiltrarPets(ListAPIView):
    #Se escoge el serializador que entrega los datos de todas las mascotas
    serializer_class = PetSerializer

    #función para filtrar en base a un identificador (en este caso rut del dueño)
    def get_queryset(self):
        id_pet = self.kwargs['owner']
        pet_list = Pet.objects.filter(
            id = id_pet
        )
        return pet_list

#Clase para Crear Mascotas Requerimiento 2
class CrearPets(CreateAPIView):
    serializer_class = PetSerializer

#Clase para Crear Mascotas Requerimiento
class UpdatePet(RetrieveUpdateAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
