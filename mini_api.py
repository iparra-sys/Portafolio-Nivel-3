from flask import Flask, jsonify
import colorama
from colorama import Fore, Style

# Inicializar colorama para colores en Windows
colorama.init(autoreset=True)

app = Flask(__name__)

# --- RUTAS DE LA API ---
@app.route("/")
def home():
    return jsonify({
        "mensaje": "Bienvenido a la Mini API 🚀",
        "endpoints": ["/saludo", "/productos"]
    })

@app.route("/saludo")
def saludo():
    return jsonify({"mensaje": "¡Hola desde la Mini API! 👋"})

@app.route("/productos")
def productos():
    lista = [
        {"id": 1, "nombre": "Laptop", "precio": 3500},
        {"id": 2, "nombre": "Mouse", "precio": 120},
        {"id": 3, "nombre": "Teclado", "precio": 200},
    ]
    return jsonify(lista)

# --- EJECUCIÓN DEL SERVIDOR ---
if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "🚀 Iniciando Mini API...")
    print(Fore.YELLOW + "📡 Escuchando en: " + Fore.GREEN + "http://127.0.0.1:5000/")
    print(Fore.MAGENTA + "🔗 Endpoints disponibles: /, /saludo, /productos\n")
    app.run(debug=True)
