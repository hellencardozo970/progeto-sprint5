import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Painel de Análise de anúncios de Carros')

df = pd.read_csv('vehicles.csv')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('A criar um histograma para o conjunto de dados de anúncios de carros')
    fig = px.histogram(df, x="price", title="Distribuição dos Preços dos Carros")
    
    st.plotly_chart(fig, use_container_width=True)