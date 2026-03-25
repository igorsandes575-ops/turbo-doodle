import streamlit as st
import pandas as pd

# Configuração visual do site
st.set_page_config(page_title="Scout-Pro AI", layout="wide")

st.title("⚽ Scout-Pro: Analisador de Palpites Profissional")
st.sidebar.header("Configurações de Banca")

# Gestão de Banca Simples
banca_total = st.sidebar.number_input("Total da sua Banca (R$)", value=1000.0)
risco_max = st.sidebar.slider("Risco por operação (%)", 1, 5, 3)

st.subheader("Análise de Partida: Time A x Time B (26/03/2026)")

col1, col2 = st.columns(2)

with col1:
    st.info("**Dados do Time A**")
    st.write("- Lesões: Jogador X (Titular), Jogador Y (Reserva)")
    st.write("- Últimos 5 jogos: V-V-E-D-V")

with col2:
    st.info("**Dados do Time B**")
    st.write("- Suspensos: Z (Zagueiro Central)")
    st.write("- Últimos 5 jogos: D-D-E-V-D")

st.success(f"**Sugestão de Aposta:** Vitória Time A. Investir: R$ {banca_total * (risco_max/100)}")
