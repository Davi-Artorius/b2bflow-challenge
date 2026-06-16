from supabase_client import get_contatos
from zapi_client import enviar_mensagem

def main():
    contatos = get_contatos()
    
    for i, contato in enumerate(contatos[:3]):
        nome = contato['nome']
        telefone = contato['telefone']
        mensagem = f"Olá, {nome} tudo bem com você?"
        
        try:
            resultado = enviar_mensagem(telefone, mensagem)
            status = "✓ Enviado" if resultado else "✗ Falha"
            print(f"[{i+1}] {nome} ({telefone}): {status}")
        except Exception as e:
            print(f"[{i+1}] {nome}: ERRO - {e}")

if __name__ == "__main__":
    main()
