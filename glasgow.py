import streamlit as st

# 1. Configuração inicial da página
st.set_page_config(page_title="Glasgow - Jade Marques", page_icon="🩺")

# 2. Estilo Visual (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .resultado-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #e3f2fd;
        border-left: 6px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Título e Introdução
st.title("🩺 Escala de Coma de Glasgow")
st.write("Avaliação do nível de consciência - Projeto de **Jade Marques**")
st.markdown("---")

# 4. Organizando a entrada de dados
st.subheader("Selecione os parâmetros:")

col1, col2, col3 = st.columns(3)

with col1:
    ocular = st.selectbox(
        "Abertura Ocular",
        options=[4, 3, 2, 1],
        format_func=lambda x: {4:"4 - Espontânea", 3:"3 - A voz", 2:"2 - À dor", 1:"1 - Nenhuma"}[x]
    )

with col2:
    verbal = st.selectbox(
        "Resposta Verbal",
        options=[5, 4, 3, 2, 1],
        format_func=lambda x: {5:"5 - Orientada", 4:"4 - Confusa", 3:"3 - Palavras inapropiadas", 2:"2 - Palavras incompreensíveis", 1:"1 - Nenhuma"}[x]
    )

with col3:
    motora = st.selectbox(
        "Resposta Motora",
        options=[6, 5, 4, 3, 2, 1],
        format_func=lambda x: {6:"6 - Obedece a comandos", 5:"5 - Localiza dor", 4:"4 - movimentos de retirada", 3:"3 - Flexão anormal", 2:"2 - Extensão anormal", 1:"1 - Nenhuma"}[x]
    )

# 5. Botão de Cálculo e Lógica
st.write("") # Espaço vazio
if st.button("CALCULAR RESULTADO"):
    total = ocular + verbal + motora
    
    if total >= 13:
        status = "TCE LEVE"
        cor_status = "#28a745" # Verde
    elif 9 <= total <= 12:
        status = "TCE MODERADO"
        cor_status = "#fd7e14" # Laranja
    else:
        status = "TCE GRAVE"
        cor_status = "#dc3545" # Vermelho

    # 6. Exibição do Resultado
    st.markdown(f"""
        <div class="resultado-card">
            <h2 style='margin:0; color:#0d47a1;'>Pontuação Total: {total}</h2>
            <p style='font-size:18px; color:{cor_status};'><b>Classificação: {status}</b></p>
        </div>
    """, unsafe_allow_html=True)

# 7. Rodapé
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("Primeiro projeto de saúde em Python desenvolvido por Jade Marques.")
