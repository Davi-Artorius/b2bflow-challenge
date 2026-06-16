import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAPI_KEY = os.getenv("ZAPI_KEY")
ZAPI_URL = "https://api.z-api.io/instances/YOUR_INSTANCE/token/YOUR_TOKEN/send-message"

def enviar_mensagem(telefone, mensagem):
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    response = requests.post(ZAPI_URL, json=payload)
    return response.status_code == 200
