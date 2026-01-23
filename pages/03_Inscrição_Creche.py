import streamlit as st
from datetime import date
import re

st.set_page_config(layout="wide", page_title="Inscreva sua Creche")

st.title("Inscrição sua Creche")
st.header("Preencha o formulário abaixo")
st.markdown("""---""")

with st.form("formCadastro"):

        nome = st.text_input("Informe seu nome:", placeholder="Preencha o seu nome")
        
        idade = st.number_input("Informe sua idade:", min_value=12, max_value=130, step=1)

        dataNascimento = st.date_input("Data de Nascimento", format="DD/MM/YYYY", min_value=date(1900, 1, 1), max_value=date.today())    

        telefone = st.text_input("Telefone / WhatsApp", placeholder="(51) 99999-9999")
    
        Creche = st.text_input("Informe o nome da creche:", placeholder="preencha o nome da Creche")
    
        rua = st.text_input("Rua / Avenida")
        
        numero = st.text_input("Número")
    
        bairro = st.text_input("Bairro")
    
        cidade = st.text_input("Cidade")
    
        estado = st.selectbox("Estado",["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA",
         "MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN",
         "RS","RO","RR","SC","SP","SE","TO"])
    
        cep = st.text_input("CEP", placeholder="00000-000")

    
        corPerfil = st.color_picker("Selecione a cor do perfil")


        btnFormCadastro = st.form_submit_button("Cadastrar")

        if btnFormCadastro:

                if not nome:
                        st.error("Preencha o nome")

                elif len(nome) <= 3:
                        st.error("Nome precisa ter pelo menos 3 letras")

                else:
                        st.success("Cadastro realizado com sucesso!")
                        st.write("Nome:", nome)
                        st.write("Idade:", idade)
                        st.write("Data de Nascimento:", dataNascimento)
                        st.write("Telefone:", telefone)
                        st.write("Nome da creche:", Creche)
                        st.write("Rua:", rua)
                        st.write("Número:", numero)
                        st.write("Bairro:", bairro)
                        st.write("Cidade:", cidade)
                        st.write("Estado:", estado)
                        st.write("CEP:", cep)
       
                        html_code = f"""
                        <h3 style='color: {corPerfil};'>
                            Essa é a cor que você escolheu para o seu perfil
                        </h3>
                        """
                        st.markdown(html_code, unsafe_allow_html=True)

