# b2bflow Python Challenge

Aplicação que lê contatos do Supabase e envia mensagens personalizadas via Z-API.

## Setup

### 1. Supabase

Crie a tabela com:

\`\`\`sql
CREATE TABLE contatos (
  id SERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  telefone TEXT NOT NULL
);
\`\`\`

### 2. Variáveis de Ambiente (.env)

\`\`\`
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_key
ZAPI_KEY=sua_key
ZAPI_INSTANCE=sua_instance
ZAPI_TOKEN=seu_token
\`\`\`

### 3. Instalar Dependências

\`\`\`bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

### 4. Rodar

\`\`\`bash
python main.py
\`\`\`

## Resultado

Envia até 3 mensagens personalizadas com o nome de cada contato.
