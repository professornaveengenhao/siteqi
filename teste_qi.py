import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Teste de QI",
    layout="centered",
)

# Estilo com imagem de fundo (custom CSS)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1581090700227-1e37b1904181?auto=format&fit=crop&w=1400&q=80');
        background-size: cover;
        background-position: center;
        color: white;
    }
    .question {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>🧠 Teste de QI Interativo</h1>", unsafe_allow_html=True)

st.write("Responda as perguntas abaixo para estimar seu raciocínio lógico. Boa sorte!")

# Inicializar pontuação e progresso
score = 0
total_questions = 5
progress = 0

# Perguntas
with st.container():
    with st.expander("1. Qual número completa a sequência: 2, 4, 8, 16, ?", expanded=True):
        q1 = st.radio("", ["18", "20", "24", "32"],index=None, key="q1")
        if q1 == "32":
            score += 1
        progress += 1
        st.progress(progress / total_questions)

with st.container():
    with st.expander("2. Se todos os gatos são felinos e alguns felinos são pretos, podemos afirmar que:", expanded=True):
        q2 = st.radio("", [
            "Todos os gatos são pretos",
            "Alguns gatos são pretos",
            "Nenhum gato é preto",
            "Não é possível afirmar"],index=None, key="q2")
        if q2 == "Não é possível afirmar":
            score += 1
        progress += 1
        st.progress(progress / total_questions)

with st.container():
    with st.expander("3. Qual letra vem a seguir? D, F, H, J, ?", expanded=True):
        q3 = st.radio("", ["K", "L", "M", "N"],index=None, key="q3")
        if q3 == "L":
            score += 1
        progress += 1
        st.progress(progress / total_questions)

with st.container():
    with st.expander("4. Qual é o resultado da expressão: (3 + 2) × (6 ÷ 2) ?", expanded=True):
        q4 = st.radio("", ["15", "10", "12", "20"],index=None, key="q4")
        if q4 == "15":
            score += 1
        progress += 1
        st.progress(progress / total_questions)

with st.container():
    with st.expander("5. Um cubo tem 6 faces. Se você pintar todas e cortar em 64 cubinhos iguais, quantos terão 3 faces pintadas?", expanded=True):
        q5 = st.radio("", ["8", "6", "12", "4"],index=None, key="q5")
        if q5 == "8":
            score += 1
        progress += 1
        st.progress(progress / total_questions)

# Resultado
if st.button("Ver Resultado"):
    st.subheader(f"🎯 Sua pontuação: {score}/5")

    if score == 5:
        st.success("QI elevado! Seu raciocínio lógico é excelente.")
    elif score >= 3:
        st.info("QI dentro da média. Bom desempenho!")
    else:
        st.warning("QI abaixo da média. Continue praticando!")
