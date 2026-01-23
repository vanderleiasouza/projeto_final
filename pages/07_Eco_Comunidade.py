import streamlit as st

st.set_page_config(
    page_title="Telhas Ecológicas",
    layout="wide"
)

# ---------- TÍTULO ----------
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
        Transformando Lixo em Solução
    </h1>
</div>
""", unsafe_allow_html=True)

st.subheader("♻️ Menos resíduos, mais futuro")

st.markdown("---")

# ---------- BLOCO 1 ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("img/foto1.png", use_container_width=True)

with col2:
    st.markdown("""
Cada **telha ecológica** produzida a partir de embalagens **Tetra Pak** reaproveita, em média, **30 a 40 embalagens** que deixariam de ir para aterros sanitários.
    """)

    st.markdown("""
### 🔢 Impacto direto:
➡️ **1.000 telhas = até 40.000 embalagens reutilizadas**  
➡️ **Toneladas de resíduos evitados por ano**
    """)

st.markdown("---")

# ---------- BLOCO 2 ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
### 🏠 Resistência que protege

As telhas feitas com embalagens **Tetra Pak** são:
- Resistentes ao **sol**
- Resistentes à **chuva**
- Resistentes à **umidade**

✔️ Não enferrujam  
✔️ Alta durabilidade  
✔️ Alternativa sustentável para coberturas
    """)

with col2:
    st.image("img/foto2.jpeg", use_container_width=True)

st.markdown("---")

# ---------- BLOCO 3 ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("img/foto3.jpeg", use_container_width=True)

with col2:
    st.markdown("""
### 🌡️ Conforto térmico e acústico

Graças à **camada de alumínio** presente nas embalagens:

✔️ Redução do calor interno  
✔️ Ambientes mais frescos  
✔️ Menor entrada de ruídos externos
    """)

st.markdown("---")

# ---------- BLOCO 4 ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
### 🤝 Renda que transforma vidas

A produção das telhas pode ser realizada por **cooperativas comunitárias**, gerando:

👷 **Trabalho local**  
💰 **Renda para famílias**  
🌍 **Economia circular na prática**
    """)

with col2:
    st.image("img/foto4.jpeg", use_container_width=True)

st.markdown("---")

# ---------- BLOCO 5 ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("img/foto5.jpeg", use_container_width=True)

with col2:
    st.markdown("""
### 📚 Educação ambiental é a base

Tudo começa com a **conscientização**.  
Ensinar crianças e comunidades a separar corretamente o lixo transforma **resíduos em recursos** e cria um futuro mais sustentável para todos.

### ♻️ Lixo que vira oportunidade

**Educação, sustentabilidade e impacto social caminhando juntos.**
    """)