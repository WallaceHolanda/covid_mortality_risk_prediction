import streamlit as st
from joblib import dump, load
import numpy as np
import os

# Definindo os Valores das Opções
radio_options = ['Sim', 'Não']
radio_values = {'Sim': 1, 'Não': 0}

vacinas_options = ['Nenhuma', '1 Dose', '2 Doses']
vacinas_values = {'Nenhuma': 0, '1 Dose': 1, '2 Doses': 2}

faixaetaria_options = ['0-11 Anos', '12-17 Anos', '18-29 Anos', '30-44 Anos', '45-59 Anos',
                       '60-74 Anos', '75-89 Anos', '> 90 Anos']

faixaetaria_values = {'0-11 Anos': 0, '12-17 Anos': 1, '18-29 Anos': 2, '30-44 Anos': 3,
                      '45-59 Anos': 4, '60-74 Anos': 5, '75-89 Anos': 6, '> 90 Anos': 7}


st.header('Modelo Óbito-Curado')
st.subheader('Preencha as seguintes informações para obter a predição de agravamento.')

# Definindo os campos de entrada
faixaetaria_value = st.radio('Qual a sua faixa-etária?', options=faixaetaria_options)
faixaetaria = faixaetaria_values.get(faixaetaria_value)

qntVacinas_value = st.radio('Quantas doses da vacina você tomou?', options=vacinas_options)
qntVacinas = vacinas_values.get(qntVacinas_value)

dorDeGarganta_value = st.radio('Possui Dor de Garganta?', options=radio_options)
dorDeGarganta = radio_values.get(dorDeGarganta_value)

dispneia_value = st.radio('Possui Dispnéia?', options=radio_options)
dispneia = radio_values.get(dispneia_value)

coriza_value = st.radio('Possui Coriza?', options=radio_options)
coriza = radio_values.get(coriza_value)

dorDeCabeca_value = st.radio('Possui Dor de Cabeça?', options=radio_options)
dorDeCabeca = radio_values.get(dorDeCabeca_value)

diabetes_value = st.radio('Possui Diabetes?', options=radio_options)
diabetes = radio_values.get(diabetes_value)

cardica_value = st.radio('Possui Problema Cardíaco?', options=radio_options)
cardica = radio_values.get(cardica_value)
