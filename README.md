
# Desplegar aplicación Flask como una función de AWS Lmabda con Zappa
En este repositorio, te guiaré paso a paso a través del proceso de despliegue utilizando Zappa, una herramienta que simplifica la integración de aplicaciones Flask con AWS Lambda.

## Requerimientos
- Phyton (por el momento Zappa solamente acepta versión de 3.6 a 3.10)
- Credenciales AWS (permisos para s3 y lambda)

## Paso a paso
### Paso 1: Configurar el entorno virtual
Crear entorno virtual

<code> python -m venv venv </code>

Activar entorno virtual (Windows)

<code> venv\Scripts\activate </code>

### Paso 2: Instalar Flask y Zappa
Dentro de tu entorno virtual, instala Flask y Zappa usando pip:

<code> pip install flask zappa</code>

### Paso 3: Crea tu aplicación Flask
Ahora, crea tu aplicación Flask en un archivo Python. En este ejemplo vamos a definir nuestro archivo app.py de la siguiente manera:

<code>
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo! Esta es la respuesta de una aplicación Flask desplegada en AWS Lambda

</code>

### Paso 4: Inicializar Zappa
Con nuestra aplicación Flask lista, inicializamos Zappa dentro del directorio de proyecto:

<code> zappa init </code>

### Paso 5: Despliegue de la aplicación Flask en AWS Lambda
Una vez que se haya configurado el archivozappa_settings.json, es hora de desplegar nuestra aplicación en AWS Lambda con el siguiente comando:

<code> zappa deploy {ambiente} </code>

Zappa se encargará de empacar la aplicación, crear los recursos necesarios en AWS y proporcionar una URL para acceder a nuestra aplicación.

## Estructura de la carpeta
demo-flask-zappa

|---- app.py

|---- requeriments.txt

|---- zappa_settings.json

|---- venv


## Documentación
Artículo en [Medium](https://medium.com/@brendagalicia/c%C3%B3mo-desplegar-aplicaciones-flask-como-aws-lambda-con-zappa-445f1a2dbd15 "Ver detalles.").

Video demo en [YouTube](https://youtu.be/AssGcpiRmA0 "Ver detalles.").
