import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Passos Mágicos", layout="wide")

st.title("📊 Previsão de Risco Educacional")
st.write("Modelo preditivo para identificar risco de defasagem educacional")

# -------------------------------------------------------------
# Carregar modelo treinado
# -------------------------------------------------------------

model = joblib.load("../model/modelo_random_forest.pkl")

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


        # Para rodar app: python -m streamlit run app.py

# Texto para explicar o funcionamento do aplicativo A aplicação desenvolvida em Streamlit utiliza um modelo de Machine Learning treinado a partir dos dados educacionais dos alunos atendidos pela Associação Passos Mágicos. O modelo foi construído utilizando o algoritmo Random Forest, que identifica padrões entre diferentes indicadores educacionais para estimar o risco de defasagem acadêmica. No aplicativo, o usuário pode inserir os principais indicadores educacionais de um aluno, como desempenho acadêmico, nível de engajamento nas atividades, aspectos psicossociais, aspectos psicopedagógicos e o indicador de ponto de virada educacional. A partir desses valores, o modelo realiza uma previsão baseada nos padrões aprendidos durante o treinamento com os dados históricos. Internamente, o algoritmo analisa as combinações entre esses indicadores e calcula a probabilidade de o aluno apresentar risco de defasagem educacional. O resultado é apresentado ao usuário de forma simples, indicando se o aluno possui baixo ou alto risco e qual a probabilidade estimada dessa condição. Essa ferramenta pode auxiliar a equipe pedagógica na identificação precoce de alunos que podem precisar de maior acompanhamento educacional. Ao identificar sinais de risco antecipadamente, é possível direcionar intervenções pedagógicas mais rápidas e personalizadas, contribuindo para melhorar o desenvolvimento acadêmico dos estudantes. Dessa forma, a aplicação funciona como um sistema de apoio à decisão educacional, permitindo que os dados coletados ao longo do programa sejam utilizados de forma estratégica para apoiar o acompanhamento dos alunos e potencializar os resultados educacionais da iniciativa.

# Versão curta (boa para o vídeo): A aplicação desenvolvida permite inserir indicadores educacionais de um aluno e, com base em um modelo de Machine Learning treinado com dados históricos, estimar a probabilidade de risco de defasagem educacional. Essa ferramenta pode auxiliar educadores a identificar alunos que necessitam de maior acompanhamento pedagógico, permitindo intervenções mais rápidas e baseadas em dados.



