import streamlit as st
import base64

st.set_page_config(page_title="Projetos", layout="wide")

st.markdown("""
<style>
.card {
    background: #9ccf7e;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
    cursor: pointer;
    margin: 30px;
}

.card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 12px 28px rgba(0,0,0,0.25);
}

.card img {
    width: 160px;
    height: 160px;
    border-radius: 50%;
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

# ---------- FUNÇÕES ----------
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def card_projeto(imagem, pagina):
    img_base64 = img_to_base64(imagem)

    if st.button(" ", key=pagina):
        st.switch_page(pagina)

    st.markdown(
        f"""
        <div class="card">
            <img src="data:image/jpeg;base64,{img_base64}">
        </div>
        """,
        unsafe_allow_html=True
    )

st.title("Nossos Projetos")
st.markdown("### Clique em um projeto para saber mais")

col1, col2 = st.columns(2) 
col3, col4 = st.columns(2)

with col1:
    card_projeto("img/logo1.jpeg", "pages/05_Educacao_Ambiental.py")

with col2:
    card_projeto("img/logo2.jpeg", "pages/06_Pequenos_Guardioes.py")

with col3:
    card_projeto("img/logo3.jpeg", "pages/07_Eco_Comunidade.py")

with col4:
    card_projeto("img/logo4.jpeg", "pages/08_Raizes_do_Futuro.py")
         