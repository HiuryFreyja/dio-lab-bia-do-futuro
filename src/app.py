import json
import streamlit as st
import pandas as pd
import requests

OLLAMA_URL = 'http://localhost:11434/api/chat'
MODELO = 'gpt-oss'  # verifique se esse modelo existe no Ollama

# ================= CARREGAR DADOS =================
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))

# ================= CONTEXTO =================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """
Você é Larissa, uma agente financeira amigável.
Dê respostas diretas (máx 3 parágrafos), práticas e baseadas nos dados.
Nunca solicite dados sensíveis.
Sempre pergunte se o problema foi resolvido.
"""

# ================= FUNÇÃO OLLAMA =================
def perguntar(msg):
    payload = {
        "model": MODELO,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{contexto}\n\nPergunta: {msg}"}
        ],
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)

    if r.status_code != 200:
        return f"Erro HTTP {r.status_code}: {r.text}"

    try:
        data = r.json()
    except Exception as e:
        return f"Erro: resposta não é JSON ({e})"

    if "message" not in data or "content" not in data["message"]:
        return f"Erro da API Ollama: {data}"

    return data["message"]["content"]



# ================= INTERFACE =================
st.title('Larissa - Agente Financeira')

if pergunta := st.chat_input('Faça sua pergunta para a Larissa'):
    st.chat_message('user').write(pergunta)

    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message('assistant').write(resposta)
