import streamlit as st
import pandas as pd

st.title(" Controle de Ganhos - Motorista de App")

st.markdown("Preencha seus ganhos mensais para ver o quanto declarar no Carnê-Leão.")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dados = []

for mes in meses:
    uber = st.number_input(f"{mes} - Ganhos Uber (R$)", min_value=0.0, step=10.0, key=f"uber_{mes}")
    noventa_nove = st.number_input(f"{mes} - Ganhos 99 (R$)", min_value=0.0, step=10.0, key=f"n99_{mes}")
    total = uber + noventa_nove
    deducao = total * 0.4
    declarar = total * 0.6
    dados.append({
        "Mês": mes,
        "Uber (R$)": uber,
        "99 (R$)": noventa_nove,
        "Total (R$)": total,
        "Dedução 40% (R$)": deducao,
        "Declarar 60% (R$)": declarar
    })

df = pd.DataFrame(dados)
st.dataframe(df.style.format({"Uber (R$)": "R$ {:.2f}", "99 (R$)": "R$ {:.2f}",
                              "Total (R$)": "R$ {:.2f}", "Dedução 40% (R$)": "R$ {:.2f}",
                              "Declarar 60% (R$)": "R$ {:.2f}"}))

st.markdown("##  Total no Ano")
st.write(f"**Ganhos Totais:** R$ {df['Total (R$)'].sum():,.2f}")
st.write(f"**Receita a Declarar:** R$ {df['Declarar 60% (R$)'].sum():,.2f}")
