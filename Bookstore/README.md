# API BOOKSTORE

## Índice

* Tecnologías y Herramientas. 
* Descripción.
* Modelo Relacional de la Base de Datos.
* Docker.
* Comandos.
* Documentación.

## Tecnologías y Herramientas

* Lenguaje: Pyhton.
* Framework: Django.
* Base de Datos: PostgreSQL.
* Editores:
  * Código: Visual Studio Code.
  * Base de Datos: DataGrip (JetBrains).
* Infraestructura local: Docker.

## Descripción

Esta es una API REST que permite la gestión de libros y autores. 
Ha sido desarrollada en Python con el framework Django y la base 
de datos PostgreSQL. 

He utilizado el software Docker para la creación de dos 
contenedores, uno para la base de datos (db) y otro para el lanzamiento
de la aplicación (web). 

A su vez he utilizado el software DataGrip para la gestión de la base de datos, 
permitiendo la creación de tablas, inserción de datos, etc. Sin embargo, esto
no es necesario ya que Django permite la creación de tablas y la inserción de 
datos mediante migraciones.

## Modelo Relacional de la Base de Datos

* **Tabla Books**:
  * id: int **_(Primary Key)_**.
  * title: string.
  * description: string.
  * author: int (devuelve el id del autor) **_(Foreign Key)_**.
  * added_at: datetime  **_(Foreign Key)_**.
  * created_at : timezone. 


* **Tabla Authors**:
  * id: int **_(Primary Key)_**.
  * name: string.
  * added_at: datetime **_(Foreign Key)_**.
  * created_at : timezone.

## Docker

* **Fichero Dockerfile**:
  * Se usa la imagen de Python 3.
  * Previene que se cree un archivo .pyc en el contenedor.
  * Se usa para que no guarde en el cache los archivos de python y asi 
  no tener que borrarlos cada vez que se haga un cambio en el codigo.
  * Creamos un directorio de trabajo en el contenedor.
  * Copiamos el archivo requirements.txt al directorio **/code**.
  * Instalamos las dependencias que se encuentran en el archivo requirements.txt.
  * Copiamos todo el contenido de la carpeta actual al directorio de trabajo 
  **/code** en el contenedor.


* **Fichero docker-compose.yml**: En este fichero se definen los servicios que se 
van a lanzar en los contenedores. En este caso se lanzan dos servicios, uno para 
la base de datos y otro para la aplicación. Con este fichero lanzamos aplicación.


* **Contenedor DB**: 
  * Imagen: postgres:latest.
  * Puerto: 5432.
  * Nombre: db.
  * Usuario: postgres.
  * Contraseña: postgres.
  * Base de Datos: bookstore.
  * Volumen: /var/lib/postgresql/data.


* **Contenedor WEB**:
  * Imagen: python: 3.8.
  * Puerto: 8000.
  * Nombre: web.
  * Comando de ejecución: python manage.py runserver.
  * Depende del contenedor db.


## Comandos 

* **Comandos en la terminal del contenedor WEB**
  * _$ docker-compose up_: Lanza los contenedores web y db (puede hacerse desde 
  la propia aplicación de Docker).
  * _$ docker-compose down_: Detiene los contenedores (puede hacerse desde 
  la propia aplicación de Docker).
  * _$ python manage.py runserver_: Lanza la aplicación (no es necesario ya que 
  este comando se ejecuta al iniciar el contenedor web).
  * _$ python manage.py makemigrations_: Crea las migraciones de la base de datos.
  * _$ python manage.py migrate_: Aplica las migraciones de la base de datos.
  * _$ python manage.py createsuperuser_: Crea un usuario administrador.
  * _$ python manage.py shell_: Abre la consola de Python.
  * _$ python manage.py startapp <app_name>_: Crea una aplicación.
  * _$ python manage.py sqlmigrate <app_name> <migration_name>_: Muestra 
  el código SQL de la migración.


* **Comandos en la terminal del contenedor DB**
  * _$ psql postgres_: Abre la consola de PostgreSQL.
  * _$ CREATE DATABASE <db_name>;_: Crea la base de datos.
  * _$ \connect <db_name>_: Conecta a la base de datos bookstore.
  * _$ \dt_: Muestra las tablas de la base de datos.
  * _$ \d <table_name>_: Muestra la estructura de la tabla.

## Documentación

* **Python**: https://docs.python.org/3/
* **Django**: https://docs.djangoproject.com/en/3.1/
* **Django REST Framework**: https://www.django-rest-framework.org/
* **PostgreSQL**: https://www.postgresql.org/docs/ 
* **Docker**: https://docs.docker.com/
* **Docker Compose**: https://docs.docker.com/compose/
* **Imagen de PostgreSQL para Docker**: https://hub.docker.com/_/postgres
* **Visual Studio Code**: https://code.visualstudio.com/docs
* **DataGrip**: https://www.jetbrains.com/help/datagrip/
