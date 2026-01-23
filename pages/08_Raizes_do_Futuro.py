import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Raízes do Futuro | Reciclagem do Óleo",
    layout="wide"
)

# TÍTULO PRINCIPAL
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
        Raízes do Futuro
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; font-size:18px;">
O que antes poluía rios e mares, hoje pode gerar renda, consciência ambiental e transformação social.
</p>
""", unsafe_allow_html=True)

st.divider()

# ==============================
# SEÇÃO 1 – IMPACTO AMBIENTAL
# ==============================
st.subheader("💧 Por que NÃO jogar óleo de cozinha na pia?")

st.write("""
Quando o óleo de cozinha é descartado de forma incorreta, ele causa sérios danos ao meio ambiente:

- ❌ **1 litro de óleo pode contaminar até 25 mil litros de água**
- ❌ Forma uma camada que impede a oxigenação da água
- ❌ Prejudica peixes, plantas aquáticas e micro-organismos
- ❌ Dificulta o tratamento da água e causa entupimentos
""")

# GRÁFICO SIMPLES 
st.subheader("📊 Impacto da poluição da água")

dados = {
    "Óleo de cozinha": 25000,
    "Esgoto doméstico": 10000,
    "Resíduos orgânicos": 5000
}

df = pd.DataFrame.from_dict(
    dados,
    orient="index",
    columns=["Litros de água contaminados"]
)

st.bar_chart(df)

st.divider()


# SEÇÃO 2 – TRANSFORMAÇÃO EM SABÃO

st.subheader("🧼 Do óleo usado ao sabão ecológico")

st.write("""
O óleo de cozinha usado pode ser reciclado e transformado em **sabão artesanal**, trazendo benefícios ambientais e sociais:

- ♻️ Reduz a poluição dos rios e mares
- 🧼 Produz sabão para uso doméstico ou comercialização
- 💰 Gera renda para famílias e cooperativas
- 🤝 Fortalece a economia local e comunitária
""")


# SEÇÃO 3 – IMAGENS DO PROCESSO
st.subheader("📸 Etapas da reciclagem do óleo")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("img/oleo.jpeg", caption="Coleta do óleo usado")

with col2:
    st.image("img/producao.jpeg", caption="corte dos sabão já pronto")

with col3:
    st.image("img/corte.jpeg", caption="embalando produtos")

with col4:
    st.image("img/final.jpeg", caption="Produto final pronto para uso ou venda")

st.divider()

# ==============================
# SEÇÃO 4 – IMPACTO SOCIAL
# ==============================
st.subheader("👨‍👩‍👧‍👦 Educação ambiental que gera renda")

st.write("""
A reciclagem do óleo de cozinha vai além do cuidado com o meio ambiente.
Ela promove **educação ambiental, inclusão social e autonomia financeira**.

✔️ Crianças aprendem desde cedo sobre sustentabilidade  
✔️ Famílias desenvolvem novas fontes de renda  
✔️ Comunidades se organizam em cooperativas  
✔️ O lixo vira oportunidade  

🌍 **Cuidar do planeta também é cuidar das pessoas.**
""")

st.success("🌱 Pequenas atitudes geram grandes transformações.")