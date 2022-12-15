#En este archivo registramos los modelos que queremos que aparezcan en el panel de administración

from django.contrib import admin
from .models import Book, Author

admin.site.register(Author)
admin.site.register(Book)

