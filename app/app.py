import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Passos Mágicos", layout="wide")

st.title("📊 Previsão de Risco Educacional")
st.write("Modelo preditivo para identificar risco de defasagem educacional")

# -------------------------------------------------------------
# Carregar modelo treinado
# -------------------------------------------------------------

model = joblib.load("model/modelo_random_forest.pkl")

# -------------------------------------------------------------
# Entrada de dados do usuário
# -------------------------------------------------------------

st.sidebar.header("Indicadores do aluno")

ida = st.sidebar.slider("Desempenho Acadêmico (IDA)", 0.0, 10.0, 5.0)
ieg = st.sidebar.slider("Engajamento (IEG)", 0.0, 10.0, 5.0)
ips = st.sidebar.slider("Indicador Psicossocial (IPS)", 0.0, 10.0, 5.0)
ipp = st.sidebar.slider("Indicador Psicopedagógico (IPP)", 0.0, 10.0, 5.0)
ipv = st.sidebar.slider("Ponto de Virada Educacional (IPV)", 0.0, 10.0, 5.0)

# -------------------------------------------------------------
# Criar dataframe com entrada
# -------------------------------------------------------------

entrada = pd.DataFrame({
    "ida":[ida],
    "ieg":[ieg],
    "ips":[ips],
    "ipp":[ipp],
    "ipv":[ipv]
})

st.subheader("Dados inseridos")

st.dataframe(entrada)

# -------------------------------------------------------------
# Fazer previsão
# -------------------------------------------------------------

if st.button("Prever risco educacional"):

    pred = model.predict(entrada)[0]

    prob = model.predict_proba(entrada)[0][1]

    if pred == 1:

        st.error(f"⚠️ Alto risco de defasagem educacional\nProbabilidade: {prob:.2%}")

    else:

        st.success(f"✅ Baixo risco de defasagem educacional\nProbabilidade: {prob:.2%}")


