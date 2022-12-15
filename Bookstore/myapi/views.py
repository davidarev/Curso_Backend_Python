#En este archivo creamos las vistas de la API REST

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id') #Obtenemos todos los objetos de la clase Author y los ordenamos por id
    serializer_class = AuthorSerializer #Indicamos el serializador que vamos a utilizar

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

