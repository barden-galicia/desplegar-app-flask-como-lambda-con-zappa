from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo! Esto es una aplicación Flask desplegada en AWS Lambda con Zappa'


@app.route('/covid')
def get_covid_data():
    global status
    try:
        api_url = 'https://disease.sh/v3/covid-19/all'
        response = requests.get(api_url)
        data = response.json()
        covid_data = {
            'pruebas': '{:,}'.format(data['tests']),
            'casos': '{:,}'.format(data['cases']),
            'recuperados': '{:,}'.format(data['recovered']),
            'fallecidos': '{:,}'.format(data['deaths'])
        }
        return jsonify({'estatus': True, 'mensaje': 'Datos obtenidos exitosamente.', 'resumen': covid_data})
    except Exception as error:
        return jsonify({'estatus': False, 'mensaje': error})