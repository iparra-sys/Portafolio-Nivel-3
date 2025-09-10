import requests
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

BASE_URL = "http://127.0.0.1:5000"

def mostrar_respuesta(endpoint):
    try:
        url = BASE_URL + endpoint
        print(Fore.YELLOW + f"\n🔗 Consultando: {url}")
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            print(Fore.GREEN + "✅ Respuesta recibida:")
            print(Fore.CYAN + str(respuesta.json()))
        else:
            print(Fore.RED + f"⚠️ Error {respuesta.status_code}: {respuesta.text}")

    except requests.exceptions.ConnectionError:
        print(Fore.RED + "❌ No se pudo conectar a la API. ¿Está corriendo mini_api.py?")

if __name__ == "__main__":
    print(Fore.MAGENTA + Style.BRIGHT + "🧪 Cliente de prueba para Mini API")
    mostrar_respuesta("/")          # Endpoint raíz
    mostrar_respuesta("/saludo")    # Endpoint saludo
    mostrar_respuesta("/productos") # Endpoint productos
