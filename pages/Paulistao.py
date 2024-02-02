import streamlit as st
import pandas as pd


df_paulistao23 = pd.read_csv("datasets/Paulistao.csv")
df_paulistao23
resultado = df_paulistao23['Resultado'].value_counts()
resultado


mandante = df_paulistao23[df_paulistao23["Mando de Campo"] == "Mandante"]
visitante = df_paulistao23[df_paulistao23["Mando de Campo"] == "Visitante"]
st.write(mandante.value_counts())
st.write(visitante.value_counts())
