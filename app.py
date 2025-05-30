import streamlit as st

st.set_page_config(page_title="Ganhos de Motorista de App", layout="centered")

st.title(" Ganhos como Motorista de App")

# Entradas de texto (evita bug do number_input)
uber_str = st.text_input("Ganhos na Uber (R$)", "0")
g99_str = st.text_input("Ganhos na 99 (R$)", "0")

# Converte string para float, trocando vírgula por ponto
try:
    uber = float(uber_str.replace(",", "."))
except:
    uber = 0.0

try:
    g99 = float(g99_str.replace(",", "."))
except:
    g99 = 0.0

# Cálculos
total = uber + g99
deducao = total * 0.40
declarar = total * 0.60

# Função para formatar no estilo brasileiro: 1.234,56
def format_brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Exibição dos resultados
st.markdown("---")
st.subheader(" Resultado")
st.write(f"**Ganhos Totais:** {format_brl(total)}")
st.write(f"**Dedução (40%):** {format_brl(deducao)}")
st.write(f"**Receita a Declarar (60%):** {format_brl(declarar)}")
