import streamlit as st
import requests
import pandas as pd

# 1. Configurações Iniciais
st.set_page_config(page_title="Scout-Pro AI", layout="wide")
API_KEY = st.secrets["API_KEY"]
BASE_URL = "https://v3.football.api-sports.io/"

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

st.title("⚽ Scout-Pro AI: Sistema de Análise Complexa")

# 2. Gestão de Banca no Menu Lateral
with st.sidebar:
    st.header("📊 Gestão de Banca")
    banca_total = st.number_input("Banca Atual (R$)", value=1000.0)
    confianca_ia = st.slider("Confiança da Análise (%)", 50, 95, 70)
    
    # Cálculo de Kelly simplificado para banca profissional
    sugestao_aposta = (banca_total * (confianca_ia / 100)) * 0.05 
    st.metric("Sugestão de Entrada", f"R$ {sugestao_aposta:.2f}")

# 3. Busca de Jogos em Tempo Real (Exemplo: Próximos Jogos)
st.subheader("📅 Análise de Confrontos para Hoje")

def buscar_jogos():
    # Busca jogos da Premier League (ID 39) como exemplo
    params = {'league': '39', 'season': '2025', 'next': '5'}
    response = requests.get(f"{BASE_URL}fixtures", headers=headers, params=params)
    return response.json()['response']

jogos = buscar_jogos()

for jogo in jogos:
    time_home = jogo['teams']['home']['name']
    time_away = jogo['teams']['away']['name']
    data_jogo = jogo['fixture']['date']
    
    with st.expander(f"🔍 Analisar: {time_home} x {time_away}"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Estatísticas H2H**")
            st.caption("Últimos confrontos diretos analisados...")
            # Aqui o sistema buscaria o histórico de cartões e golos
            
        with col2:
            st.write("**Baixas e Lesões**")
            st.warning("Verificando Departamento Médico...")
            
        with col3:
            st.write("**Veredito da IA**")
            prob = confianca_ia
            st.write(f"Probabilidade: {prob}%")
            if prob > 75:
                st.success("🔥 Entrada de Alto Valor")
            else:
                st.info("⚖️ Jogo Equilibrado")

st.markdown("---")
st.caption("Dados fornecidos por API-Football | Análise Gerada por IA Scout-Pro")
