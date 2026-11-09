from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- 1. Importar la librería
from asistente import obtener_respuesta_asistente

app = Flask(__name__)
CORS(app)  # <--- 2. Habilitar CORS para permitir la conexión desde GitHub Pages

@app.route('/chat', methods=['POST'])
def chat():
    datos = request.get_json()
    mensaje = datos.get('mensaje', '')
    estado = datos.get('estado', {})
    
    respuesta, nuevo_estado = obtener_respuesta_asistente(mensaje, estado)
    return jsonify({'respuesta': respuesta, 'estado': nuevo_estado})

if __name__ == '__main__':
    app.run(debug=True)