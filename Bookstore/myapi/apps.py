#En este archivo se define la configuración de la aplicación de la API REST de Django

from django.apps import AppConfig

class MyapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Esto es para que no salga un warning
    name = 'myapi' #Nombre de la app
