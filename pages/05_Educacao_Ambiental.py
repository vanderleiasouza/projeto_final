import streamlit as st

st.set_page_config(
    page_title="Educação Ambiental | Futuras Gerações",
    layout="centered"
)

st.markdown("""
<style>
.titulo-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
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
        Educação Ambiental
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; font-size:18px;">
Cuidar do planeta hoje é garantir vida, equilíbrio e oportunidades para as futuras gerações.
</p>
""", unsafe_allow_html=True)

st.divider()

# SEÇÃO 1
st.subheader("🌍 Por que a Educação Ambiental é tão importante?")

st.write("""
A educação ambiental forma cidadãos conscientes, responsáveis e comprometidos com o futuro do planeta.
Ela nos ajuda a entender que nossas escolhas diárias impactam diretamente a natureza e a qualidade de vida das próximas gerações.

Educar é plantar hoje o cuidado que será colhido amanhã.
""")

# SEÇÃO 2
st.subheader("💧 Uso consciente dos recursos naturais")

st.write("""
Os recursos naturais não são infinitos.
Água, solo, florestas e energia precisam ser utilizados com responsabilidade.

Pequenas atitudes fazem grande diferença:
- Economizar água e energia
- Separar corretamente os resíduos
- Reutilizar e reciclar sempre que possível
""")

# SEÇÃO 3
st.subheader("🛍️ Consumismo x Consumo consciente")

st.write("""
O consumismo excessivo gera desperdício, poluição e exploração desenfreada dos recursos naturais.

Já o consumo consciente nos convida a refletir:
- Eu realmente preciso disso?
- De onde vem o que consumo?
- Qual impacto isso gera no meio ambiente e na sociedade?

Consumir menos e melhor é um ato de cuidado com o planeta.
""")

# SEÇÃO 4
st.subheader("🌱 Desenvolvimento e preservação podem caminhar juntos")

st.write("""
É possível crescer, inovar e gerar renda sem destruir a natureza.
O desenvolvimento sustentável busca equilíbrio entre:
- Crescimento econômico
- Inclusão social
- Preservação ambiental

Quando pensamos a longo prazo, proteger o meio ambiente é investir no futuro.
""")

# SEÇÃO 5 – ODS
st.subheader("🌐 As ODS e a Educação Ambiental")

st.write("""
As **Objetivos de Desenvolvimento Sustentável (ODS)** fazem parte da Agenda 2030 da ONU
e mostram que cuidar do planeta está diretamente ligado à qualidade de vida das pessoas.

A educação ambiental se conecta com várias ODS, como:
- ODS 4 – Educação de Qualidade
- ODS 6 – Água Potável e Saneamento
- ODS 11 – Cidades e Comunidades Sustentáveis
- ODS 12 – Consumo e Produção Responsáveis
- ODS 13 – Ação Contra a Mudança Global do Clima

Tudo está interligado.
""")

st.success("🌎 Educar hoje é preservar o amanhã.")
