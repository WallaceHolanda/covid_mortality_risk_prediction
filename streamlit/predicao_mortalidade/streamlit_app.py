import streamlit as st
import streamlit.components.v1 as components
import modelo as md
import componentes as componentes
import joblib
import sklearn
import numpy as np
import pandas as pd
import os
from PIL import Image

modeloAB = md.criaAdaBoost()
modeloRF = md.criaRandomForest()
modeloLR = md.criaRegressao()
modeloGB = md.criaGradientBoosting()

# Definindo os Valores do Modelo
modelo_values = {'Gradient Boosting': modeloGB, 
                 'Random Forest': modeloRF, 
                 'Logistic Regression': modeloLR, 
                 'Ada Boost': modeloAB}

# Construção da Página
componentes.imagemCabecalho()   
componentes.cabecalhoPagina()

# Campos do Formulário
componentes.exibirPergunta('Choose the Prediction Model')
modelo_value = st.selectbox('id_modelo', options=componentes.modelo_options, label_visibility='collapsed')
modeloSelecionado = modelo_values.get(modelo_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('What is your age range?')
faixaetaria_value = st.radio('id_idade', options=componentes.faixaetaria_options, label_visibility='collapsed')
faixaetaria = componentes.faixaetaria_values.get(faixaetaria_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('How many doses of the vaccine have you taken?')
qntVacinas_value = st.radio('id_vacinas', options=componentes.vacinas_options, label_visibility='collapsed')
qntVacinas = componentes.vacinas_values.get(qntVacinas_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('How many days have passed since the first symptom?')
faixaDiasSintomas_value = st.radio('id_sintomas', options=componentes.faixaDiasSintomas_options, label_visibility='collapsed')
faixaDiasSintomas = componentes.faixaDiasSintomas_values.get(faixaDiasSintomas_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('Do you have sore throat?')
dorDeGarganta_value = st.radio('id_garganta', options=componentes.radio_options, label_visibility='collapsed')
dorDeGarganta = componentes.radio_values.get(dorDeGarganta_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('Do you have headache?')
dorDeCabeca_value = st.radio('id_cabeca', options=componentes.radio_options, label_visibility='collapsed')
dorDeCabeca = componentes.radio_values.get(dorDeCabeca_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('Do you have body aches?')
dorNoCorpo_value = st.radio('id_corpo', options=componentes.radio_options, label_visibility='collapsed')
dorNoCorpo = componentes.radio_values.get(dorNoCorpo_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('Do you have runny nose?')
coriza_value = st.radio('id_coriza', options=componentes.radio_options, label_visibility='collapsed')
coriza = componentes.radio_values.get(coriza_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('Do you have difficulty breathing (dyspnea)?')
dispneia_value = st.radio('id_dispneia', options=componentes.radio_options, label_visibility='collapsed')
dispneia = componentes.radio_values.get(dispneia_value)
componentes.adicionarSeparador()

componentes.exibirPergunta('Do you have diabetes?')
diabetes_value = st.radio('id_diabetes', options=componentes.radio_options, label_visibility='collapsed')
diabetes = componentes.radio_values.get(diabetes_value)
componentes.adicionarSeparador()

# st.write(dorDeCabeca, cardica)
# faixaDiasSintomas, diabetes, 
dados = {
    'faixaetaria': faixaetaria,
    'qntVacinas': qntVacinas,
    'dorDeGarganta': dorDeGarganta,
    'dorDeCabeca': dorDeCabeca,
    'coriza': coriza,
    'dispneia': dispneia,
    'diabetes': diabetes,
    'faixaDiasSintomas': faixaDiasSintomas,
}

modelo = md.importarModelo(modeloSelecionado)
botao = st.button('Perform Prediction')
if(botao):
    # dadosFormatados = np.array([[dados]])
    dadosFormatados = pd.DataFrame([dados])
    resultado = modelo.predict_proba(dadosFormatados)
    probAgravamento =  round(resultado[0][0] * 100, 3)
    componentes.exibirProbabilidade(str(probAgravamento))
    # st.write('Dados: ', dadosFormatados)

componentes.adicionarSeparador()
componentes.exibirFooter()