import streamlit as st
import pandas as pd


st.set_page_config(page_title="Projeto Íris - SSIT UnB", page_icon="👁️", layout="wide")

# Estilização CSS 
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #004587; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BACKEND SIMULADO ---
# Dados baseados no Relatório Técnico 
LISTA_SUJA_2026 = ["12.345.678/0001-90", "23.456.789/0001-00", "45.678.901/0001-12"]
GATILHOS_RISCO = ["viagem imediata", "ganhos altos", "sem experiência", "documentos originais", "pagamento antecipado"]

# --- SIDEBAR ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/2/21/IEEE_logo.svg", width=100)
st.sidebar.title("Painel de Controle")
st.sidebar.info("Projeto Íris: Otimização Preditiva contra o Trabalho Escravo Urbano[cite: 26, 33].")
st.sidebar.metric(label="Acurácia do Modelo (LightGBM)", value="87.4%", delta="1.2%")
st.sidebar.write("**Status da Base:** Atualizada em Abr/2026[cite: 90].")

# --- ÁREA PRINCIPAL ---
st.title("👁️ Sistema de Triagem Preditiva Íris")
st.write("Ferramenta interna para análise de vagas suspeitas e apoio à fiscalização do MTE[cite: 36, 54].")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Análise de Anúncio")
    texto_vaga = st.text_area("Cole aqui o texto do anúncio coletado (Web Scraping):", height=200, 
                              placeholder="Ex: Vaga internacional com tudo pago, início imediato...")
    
    cnpj_vaga = st.text_input("CNPJ ou Nome da Empresa para conferência:", placeholder="00.000.000/0001-00")

with col2:
    st.subheader("Critérios de Risco")
    st.write("- Cruzamento com Cadastro de Empregadores.")
    st.write("- Detecção Semântica de Gatilhos[cite: 61].")
    st.write("- Verificação de Redes de Dispersão[cite: 78].")

if st.button("EXECUTAR ANÁLISE PREDITIVA"):
    st.divider()
    
    # Lógica de Verificação
    encontrado_lista = cnpj_vaga in LISTA_SUJA_2026
    gatilhos_encontrados = [g for g in GATILHOS_RISCO if g in texto_vaga.lower()]
    
    if encontrado_lista:
        st.error("🚨 **ALERTA CRÍTICO: EMPRESA IDENTIFICADA NA LISTA SUJA**")
        st.write(f"O CNPJ {cnpj_vaga} consta no Cadastro de Empregadores infratores atualizado em 2026.")
    
    if gatilhos_encontrados:
        st.warning(f"⚠️ **SINAIS DE ALERTA DETECTADOS NO TEXTO**")
        st.write("Gatilhos de aliciamento encontrados:")
        for g in gatilhos_encontrados:
            st.write(f"- {g.capitalize()}")
        st.info("Nota: Estes padrões coincidem com as iscas de aliciamento digital mapeadas.")
        
    if not encontrado_lista and not gatilhos_encontrados:
        st.success("Análise concluída: Nenhum padrão de risco imediato detectado.")