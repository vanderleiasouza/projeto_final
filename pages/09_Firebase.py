import streamlit as st
from google.cloud import firestore

st.title ("Banco de dados")

baseDados = firestore.Client.from_service_account_json("firebase.json")

# -- Formulário de Cadastro
with st.form("formFirebase"):

    nome = st.text_input("Nome:", placeholder="Preencha o seu nome...")
    apelido = st.text_input("Apelido", placeholder="Digite seu apelido...")
    senha = st.text_input("Senha", placeholder="Informe sua senha...", type="password")
        
    btnSalvarUsuario = st.form_submit_button("Salvar", use_container_width=True)

    if btnSalvarUsuario:
        if nome and  apelido and senha:
            #salvar no banco de dados
            novoUsuario = baseDados.collection("usuarios").document(apelido)
            novoUsuario.set(
                {
                    "nome": nome,
                    "apelido": apelido,
                    "senha": senha,   
                }
            )
            st.sucess("Usuário Cadastrado!")
        else:
            st.error("Informe seu Nome, Apelido e Senha, por favor")

"---"

usuarios = baseDados.collection("usuarios").stream()

for usuarioRef in usuarios:

    usuario = usuarioRef.to_dict()
    nomeUsuario = usuario ("nome")
    apelidoUsuario = usuario ("apelido")
    st.subheader(f"Usuário {apelidoUsuario}")
    st.write(f":material/person: Nome: {nomeUsuario} com {apelidoUsuario}")





            