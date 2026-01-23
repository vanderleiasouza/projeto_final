import streamlit as st

st.set_page_config(page_title="Educação Ambiental: Do Lixo ao Brinquedo", layout="wide")

st.title("♻️ Transformando o Futuro: Educação Ambiental na Infância")

st.markdown("""
A educação ambiental nas creches e escolas é o primeiro passo para uma sociedade sustentável. 
Quando uma criança aprende a separar o lixo, ela se torna uma **multiplicadora**, levando esse 
conhecimento para dentro de casa e transformando os hábitos de toda a família.
""")

st.markdown("""
<style>
.titulo-container {
    display: flex;
    align-items: center;
    justify-content: flex-start; /* esquerda */
    gap: 12px;
    padding-left: 20px; /* afastamento da borda */
}

.plantinha {
    font-size: 50px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}
</style>

<div class="titulo-container">
    <div class="plantinha">🌱</div>
    <h1 style="color:#2e7d32; margin:0;">
        Da Horta à Merenda
    </h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Insira aqui a foto das crianças separando lixo orgânico/compostagem
    st.image("img/criancas1.jpeg", caption="Crianças aprendendo sobre compostagem")
    st.image("img/criancas3.jpeg", caption="Crianças aprendendo sobre plantar")
   


with col2:
    st.image("img/criancas4.jpeg", caption="Crianças aprendendo sobre colher")
    st.image("img/criancas5.jpeg", caption="Crianças comendo os legumes que plantaram")
    
    


st.subheader("O Impacto do Orgânico")
st.write("""
    No Brasil, cerca de **45,3% a 51,4%** de todo o lixo gerado é composto por resíduos orgânicos. 
    Infelizmente, **apenas cerca de 1%** desse material é reaproveitado via compostagem. 
    
    Ao ensinar as crianças a compostar:
    * Reduzimos a pressão sobre aterros sanitários saturados.
    * Produzimos adubo rico para hortas escolares.
    * Estimulamos uma alimentação mais saudável e o contato com a natureza.
    """)

# --- SEÇÃO 2: Reciclagem e Criatividade ---
st.header("🎨 Transformando Descarte em Diversão")

col4, col5 = st.columns(2)

with col4:
    st.image("img/criancas0.jpeg", caption="Crianças aprendendo a separar o lixo reciclável")
    st.write("""
    ### Por que Brinquedos Recicláveis?
    Brincar com materiais como garrafas PET e papelão estimula a **criatividade** e a **coordenação motora** mais do que brinquedos prontos.
    
    **Dados sobre a Reciclagem no Brasil:**
    * Cada brasileiro produz, em média, **1 kg de lixo por dia**.
    * Menos de **10%** desse lixo é efetivamente reciclado no país.
    * Mais de **70%** dos brasileiros ainda não possuem o hábito de separar o lixo.
    """)
    st.info("💡 Quando a criança fabrica seu próprio brinquedo, ela entende o valor do consumo consciente.")

with col5:
    # Insira aqui a foto das crianças brincando com brinquedos de PET/Papelão
    
    st.image("img/criancas2.jpeg", caption="Criatividade sem limites com materiais reciclados")

