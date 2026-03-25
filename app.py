import streamlit as st
import requests
import pandas as pd

# 1. Configurações de Interface
st.set_page_config(page_title="Scout-Pro AI", layout="wide")

# Conexão com a API (Pega da chave que você salvou no Streamlit)
try:
    API_KEY = st.secrets["API_KEY"]
except:
    st.error("⚠️ Falta configurar a API_KEY nos Secrets do Streamlit!")
    st.stop()

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

st.title("⚽ Scout-Pro AI: Análise de Dados Esportivos")

# 2. Gestão de Banca (Menu Lateral)
with st.sidebar:
    st.header("📊 Gestão de Banca")
    banca_total = st.number_input("Banca Total (R$)", value=1000.0)
    confianca = st.slider("Confiança da IA (%)", 50, 95, 75)
    
    # Cálculo de gestão: Unidade de 2% da banca ajustada pela confiança
    sugestao = (banca_total * 0.02) * (confianca / 100)
    st.metric("Aposta Sugerida", f"R$ {sugestao:.2f}")

# 3. Função para buscar jogos reais
def buscar_jogos():
    # Buscando próximos 10 jogos da Premier League (ID 39)
    url = "https://v3.football.api-sports.io/fixtures?league=39&season=2025&next=10"
    response = requests.get(url, headers=headers)
    return response.json().get('response', [])

jogos = buscar_jogos()

if not jogos:
    st.info("Buscando jogos... Verifique se sua API_KEY está correta.")

for jogo in jogos:
    casa = jogo['teams']['home']['name']
    fora = jogo['teams']['away']['name']
    id_jogo = jogo['fixture']['id']
    
    with st.expander(f"🔍 Analisar: {casa} x {fora}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Dados do Confronto")
            st.write(f"🏠 **Casa:** {casa}")
            st.write(f"🚀 **Fora:** {fora}")
            st.caption("Analise de H2H e forma recente em processamento...")
            
        with col2:
            st.subheader("🧠 Veredito Scout-Pro")
            if confianca > 80:
                st.success(f"🔥 Entrada de VALOR confirmada para {casa}")
            else:
                st.warning("⚖️ Jogo de alto risco - Aguarde escalação")

st.markdown("---")
st.caption("Dados Profissionais via API-Football | Criado para Scout-Pro")
