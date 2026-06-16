from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL e SUPABASE_KEY são obrigatórios no .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_contatos():
    try:
        response = supabase.table("contatos").select("*").execute()
        if not response.data:
            print("Aviso: Nenhum contato encontrado na tabela.")
            return []
        return response.data
    except Exception as e:
        print(f"Erro ao buscar contatos do Supabase: {e}")
        raise
