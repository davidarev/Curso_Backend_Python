#En este archivo creamos las urls de cada vista para acceder a la API REST

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() #Creamos un router
#Registramos las vistas de la APIs. El primer parámetro es la ruta de la API y el segundo es la vista que vamos a utilizar
router.register(r'authors', views.AuthorViewSet) # "http://localhost:8000/authors"
router.register(r'books', views.BookViewSet) # "http://localhost:8000/books"

urlpatterns = [
    path('', include(router.urls)), #Añadimos la ruta de la API
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')), #Añadimos la ruta de la autenticación
]