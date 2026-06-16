import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")

def enviar_mensagem(telefone, mensagem):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/send-message"
    headers = {"Authorization": f"Bearer {ZAPI_TOKEN}"}
    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            return True
        else:
            print(f"Z-API erro {response.status_code}: {response.text[:100]}")
            return False
    except requests.exceptions.Timeout:
        print(f"Timeout ao enviar para {telefone}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão Z-API: {e}")
        return False
