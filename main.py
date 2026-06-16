from supabase_client import get_contatos
from zapi_client import enviar_mensagem

def main():
    contatos = get_contatos()

    if not contatos:
        print("Nenhum contato para processar.")
        return

    contador = 0
    for contato in contatos:
        if contador >= 3:
            break

        nome = contato.get('nome', '').strip()
        telefone = contato.get('telefone', '').strip()

        if not nome or not telefone:
            print(f"[IGNORADO] Contato incompleto (nome ou telefone vazio)")
            continue

        if not telefone.isdigit():
            print(f"[IGNORADO] {nome} - telefone inválido: {telefone}")
            continue

        mensagem = f"Olá, {nome} tudo bem com você?"

        try:
            resultado = enviar_mensagem(telefone, mensagem)
            status = "✓ Enviado" if resultado else "✗ Falha"
            print(f"[{contador+1}] {nome} ({telefone}): {status}")
            contador += 1
        except Exception as e:
            print(f"[{contador+1}] {nome}: ERRO - {e}")

if __name__ == "__main__":
    main()
