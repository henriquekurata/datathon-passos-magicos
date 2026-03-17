# Datathon - Passos Mágicos

Projeto de **Data Analytics e Machine Learning** desenvolvido para o Datathon da Pós-Tech com o objetivo de analisar dados educacionais e prever risco de defasagem acadêmica em alunos atendidos pela **Associação Passos Mágicos**.

---

# Contexto

A Associação Passos Mágicos atua na transformação da vida de crianças e jovens de baixa renda por meio da educação.

Com base em dados educacionais coletados entre **2022 e 2024**, este projeto busca utilizar técnicas de **análise de dados e machine learning** para compreender fatores que influenciam o desenvolvimento educacional dos alunos.

---

# Objetivo do Projeto

O objetivo deste projeto é:

- Analisar indicadores educacionais dos alunos
- Identificar padrões de desempenho acadêmico
- Entender fatores associados à defasagem educacional
- Desenvolver um modelo preditivo de risco educacional
- Criar uma aplicação interativa para apoio à decisão pedagógica

---

# Base de Dados

O dataset contém informações educacionais dos anos:

- 2022
- 2023
- 2024

Principais indicadores analisados:

| Indicador | Descrição |
|--------|--------|
| IDA | Indicador de Desempenho Acadêmico |
| IEG | Indicador de Engajamento |
| IPS | Indicador Psicossocial |
| IPP | Indicador Psicopedagógico |
| IPV | Indicador de Ponto de Virada |
| IAN | Indicador de Adequação de Nível |

---

# Análise Exploratória de Dados

Durante a análise exploratória foram avaliados diversos aspectos do desenvolvimento educacional.

Principais análises realizadas:

- Evolução do desempenho acadêmico ao longo dos anos
- Relação entre engajamento e desempenho acadêmico
- Perfil de defasagem educacional dos alunos
- Correlação entre indicadores educacionais

Principais visualizações utilizadas:

- Evolução do **IDA**
- Relação entre **IEG vs IDA**
- Perfil de **defasagem educacional (IAN)**
- **Heatmap de correlação** entre indicadores

---

# Feature Engineering

Foram criadas variáveis adicionais para auxiliar na modelagem:

- média das notas das disciplinas
- classificação de níveis de defasagem educacional
- criação da variável alvo para previsão de risco

A variável alvo utilizada no modelo foi **risco de defasagem educacional**, considerando alunos com maior nível de defasagem como grupo de risco.

---

# Modelos de Machine Learning

Foram avaliados dois modelos de classificação:

### Regressão Logística

Modelo base utilizado para análise inicial dos dados.

### Random Forest

Modelo que apresentou melhor desempenho na identificação de alunos em risco de defasagem educacional.

Principais métricas utilizadas:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Curva ROC

---

# Importância das Variáveis

O modelo Random Forest identificou os seguintes indicadores como mais relevantes:

- **IPV (Ponto de Virada Educacional)**
- **IDA (Desempenho Acadêmico)**
- **IEG (Engajamento nas atividades)**

Esses indicadores apresentam maior influência na previsão do risco educacional.

---

# Aplicação Streamlit

Foi desenvolvida uma aplicação interativa utilizando **Streamlit**.

A aplicação permite:

- Inserir indicadores educacionais de um aluno
- Calcular a probabilidade de risco de defasagem
- Apoiar decisões pedagógicas baseadas em dados

Para executar a aplicação:

```bash
streamlit run app/app.py

---

app/
    app.py

data/
    2022.xlsx
    2023.xlsx
    2024.xlsx

model/
    modelo_random_forest.pkl

notebooks/
    analise_datathon.ipynb

presentation/
    slides_datathon.pptx

README.md
requirements.txt