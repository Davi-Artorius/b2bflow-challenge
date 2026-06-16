import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAPI_KEY = os.getenv("ZAPI_KEY")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-message"

def enviar_mensagem(telefone, mensagem):
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    response = requests.post(ZAPI_URL, json=payload)
    return response.status_code == 200
