import json
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Cargar los datos desde el archivo JSON
def load_car_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("data.json not found. Make sure the file is in the correct location.")
        return []
    except json.JSONDecodeError:
        logging.error("Error decoding data.json. Ensure it is a valid JSON file.")
        return []

car_data = load_car_data()

# Índice para simular "streaming" de datos
current_index = 0

@app.route('/api/next_state', methods=['GET'])
def get_next_state():
    global current_index

    # Comprueba si hay datos disponibles
    if current_index >= len(car_data):
        return jsonify({"message": "No more data available"}), 404

    # Devuelve el siguiente estado
    next_state = car_data[current_index]

    # Incrementa el índice para el próximo dato
    current_index += 1

    return jsonify(next_state)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
