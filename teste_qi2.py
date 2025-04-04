import streamlit as st
import json

st.set_page_config(page_title="Teste Completo de QI", layout="centered")


st.markdown(
    """
    <style>
    /* Estilização automática com base no tema do sistema */

    @media (prefers-color-scheme: dark) {
        html, body, .stApp, [class*="css"] {
            color: white !important;
            background-color: #0e1117;
        }
    }

    @media (prefers-color-scheme: light) {
        html, body, .stApp, [class*="css"] {
            color: black !important;
            background-color: white;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar perguntas
@st.cache_data
def carregar_perguntas():
    with open("perguntas.json", "r", encoding="utf-8") as file:
        return json.load(file)

perguntas = carregar_perguntas()

st.title("🧠 Teste de QI Completo")
st.markdown("Você responderá 25 questões. Boa sorte!")

# Inicializar variáveis
if "respostas" not in st.session_state:
    st.session_state.respostas = {}

for pergunta in perguntas:
    pergunta_id = f"q{pergunta['id']}"
    if pergunta_id not in st.session_state.respostas:
        st.session_state.respostas[pergunta_id] = None

# Exibir perguntas com barra de progresso
for pergunta in perguntas:
    resposta = st.radio(
        f"{pergunta['id']}. {pergunta['pergunta']}",
        pergunta["opcoes"],
        index=None,
        key=f"q{pergunta['id']}"
    )

    st.session_state.respostas[f"q{pergunta['id']}"] = resposta
    progresso = sum(1 for r in st.session_state.respostas.values() if r is not None)
    st.progress(progresso / len(perguntas))

# Resultado
if st.button("Ver resultado"):
    acertos = 0
    for pergunta in perguntas:
        key = f"q{pergunta['id']}"
        if st.session_state.respostas[key] == pergunta["correta"]:
            acertos += 1

    st.subheader(f"✅ Você acertou {acertos} de {len(perguntas)}")

    if acertos == len(perguntas):
        st.success("QI excepcional!")
    elif acertos >= len(perguntas) * 0.75:
        st.info("QI elevado, excelente desempenho!")
    elif acertos >= len(perguntas) * 0.5:
        st.warning("QI dentro da média.")
    else:
        st.error("QI abaixo da média. Continue praticando!")