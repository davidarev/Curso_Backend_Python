#En este archivo registramos los modelos y sus respectivos campos en la base de datos

from django.db import models
from django.utils import timezone
from django.conf import settings

#Tabla Author
class Author(models.Model):
    #Definimos los campos de la tabla
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

#Tabla Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
     return self.title
