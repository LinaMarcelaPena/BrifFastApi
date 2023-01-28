# BrifFastApi

# Python virtualenv (VenV)

Es una herramienta que se utiliza para crear entornos
virtuales aislados en Python. Este entorno tiene su 
propia ruta de instalación y no comparte sus bibliotecas
con otros entornos

# Verificaciones antes:

Verificar que Python este correctamente instalado.
Símbolo de sistema, escribir:
python --versión

# Instalar o actualizar PIP

Símbolo de sistema:
actualizar - pip install  --upgrade pip
instalar pip install   pip


# Instalar entorno virtual
pip install virtualenv

# Crear el entorno virtual
1. Crear una carpeta donde se guardara el entorno virtual
2. ir a Símbolo de sistema y dirigirnos desde esta a la ruta donde creamos la carpeta 
3. Escribir el siguiente comando:
python  -m venv venv - Crea una carpeta que contiene todos los ejecutables necesarios para usar los paquetes que necesitaría un proyecto de Python.

python - debemos esribir nuestra version de python ejemplo python3  o en algunas ocaciones funciona solo con python
ultimo venv - nombre de la carpeta donde se guardaran los paquetes que necesita el proyecto.

4.  Despues de ejecutar este comando actualizamos la carpeta la cual ya tendra los ejecutables necesarios para nuestro proyecto 
La carpeta :

Include -  en esta se van a guardar las demas librerias que vamos a usar 

lib- dentro de esta se encuentra site-packages la ubicación donde Python instala sus módulos.

Script - Comandos que podemos usar, dentro de estos se encuentra el active que se usa para iniciar el entorno de desarrollo.

# activar entorno virtual

venv\Scripts\activate 
Verificar si esta es la ruta donde se encuentra el activate


# crear archivo main.py con hola mundo 


# uvicorn
Una librería que funciona como servidor, permite a nuestra computadora 
tenga como funcion de servidor.

# instalar uvicorn

pip install uvicorn

# levantar el servidor 
uvicorn main:app --reload

uvicorn	 Librería que permite el deploy web		
main Nombre del archivo , main.py (el "módulo" de Python).
:app Nombre de la instancia, el objeto creado dentro de main.py con la línea app = FastAPI().	
–reload  Permite la recarga automática  después de hacer cambios

