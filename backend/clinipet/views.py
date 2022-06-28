from django.shortcuts import render

from .models import Pet
from rest_framework.generics import (ListAPIView,CreateAPIView,RetrieveUpdateAPIView)
from rest_framework import generics
from rest_framework import status

from .serializers import PetSerializer


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
    """Es ta es la clase FiltrarPets, la cual recibe un objeto de tipo ListAPIView y, luego de escoger el serializador 
    que entrega los datos de todas las mascotas, utiliza la función get_queryset para filtrar, en base al rut del dueño
    de la mascota.

    Args:
        ListAPIView (_type_): Proporciona un control del método Get, se utiliza para endpoints de solo lectura
    Returns:
        pet_list: Lista que contiene las mascotas del modelo Pet
    """

    serializer_class = PetSerializer

    def get_queryset(self):
        """Esta es una función que accede al modelo Pet y posteriormente retorna todos los objetos del mismo que tienen por 
        dueño el que tiene el rut correspondiente

        Returns:
            pet_list: Lista que contiene las mascotas del modelo Pet
        """
        id_pet = self.kwargs['owner']
        pet_list = Pet.objects.filter(
            id = id_pet
        )
        return pet_list

class CrearPets(CreateAPIView):
    """Esta es la clase CrearPets, y su función es crear Mascotas

    Args:
        CreateAPIView: Vista concreta para crear una instancia de modelo
    """
    serializer_class = PetSerializer


class UpdatePet(RetrieveUpdateAPIView):
    """Esta es la clase UpdatePet, y su función es actualizar una Mascota

    Args:
        RetrieveUpdateAPIView: Vista concreta para recuperar, actualizar una instancia de modelo
    """
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
