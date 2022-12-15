#En este archivo registramos los modelos que queremos que aparezcan en el panel de administración de la API REST

from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.HyperlinkedModelSerializer): #Creamos el serializador
    class Meta:
        model = Author #Indicamos el modelo que vamos a serializar
        fields = ('id', 'name') #Indicamos los campos que queremos que se muestren en la API

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author')
