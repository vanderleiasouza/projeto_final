import streamlit as st
from streamlit_option_menu import option_menu
import base64


#imagem de plano de fundo
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# CHAMADA DA FUNÇÃO
set_background("img/capa.jpg")

st.markdown(
    """
    <h1 style="
        text-align: center;
        color: #ffffff;
        font-size: 40px;
    ">
        Educação Ambiental em Creches e Comunidade Local
    </h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style="
        text-align: center;
        color: #ffffff;
        font-size: 18px;
    ">
        Venha você também fazer parte dessa ação!
    </h1>
    """,
    unsafe_allow_html=True
)

"---"


st.write("Você escolheu:", optionMenu)
