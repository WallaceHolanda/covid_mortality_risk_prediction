import streamlit as st
import streamlit.components.v1 as components
import modelo as md
import componentes as comp
import joblib
import sklearn
import numpy as np
import pandas as pd
import os

modeloAB = md.criaAdaBoost()
modeloRF = md.criaRandomForest()
modeloLR = md.LogisticRegression()
modeloGB = md.criaGradientBoosting()

modelo_values = {'Gradient Boosting': modeloGB, 
                 'Random Forest': modeloRF, 
                 'Logistic Regression': modeloLR, 
                 'Ada Boost': modeloAB}

# Construção da Página
comp.imagemCabecalho()   
comp.cabecalhoPagina()

# Definindo os campos de entrada
comp.exibirPergunta('Escolha o Modelo a ser utilizado')
modelo_value = st.selectbox('id_modelo', options=comp.modelo_options,label_visibility='collapsed')
modeloSelecionado = modelo_values.get(modelo_value)
comp.adicionarSeparador()

comp.exibirPergunta('Qual a sua faixa-etária?')
faixaetaria_value = st.radio('id_idade', options=comp.faixaetaria_options,label_visibility='collapsed')
faixaetaria = comp.faixaetaria_values.get(faixaetaria_value)
comp.adicionarSeparador()

comp.exibirPergunta('Quantas doses da vacina você tomou?')
qntVacinas_value = st.radio('id_vacina', options=comp.vacinas_options,label_visibility='collapsed')
qntVacinas = comp.vacinas_values.get(qntVacinas_value)
comp.adicionarSeparador()

comp.exibirPergunta('Quantos dias se passaram desde o primeiro sintoma?')
faixaDiasSintomas_value = st.radio('id_sintomas', options=comp.faixaDiasSintomas_options,label_visibility='collapsed')
faixaDiasSintomas = comp.faixaDiasSintomas_values.get(faixaDiasSintomas_value)
comp.adicionarSeparador()

comp.exibirPergunta('Apresenta Dor de Garganta?')
dorDeGarganta_value = st.radio('id_garganta', options=comp.radio_options,label_visibility='collapsed')
dorDeGarganta = comp.radio_values.get(dorDeGarganta_value)
comp.adicionarSeparador()

comp.exibirPergunta('Apresenta Dor de Cabeça?')
dorDeCabeca_value = st.radio('id_cabeca', options=comp.radio_options,label_visibility='collapsed')
dorDeCabeca = comp.radio_values.get(dorDeCabeca_value)
comp.adicionarSeparador()

comp.exibirPergunta('Apresenta Coriza?')
coriza_value = st.radio('id_coriza', options=comp.radio_options,label_visibility='collapsed')
coriza = comp.radio_values.get(coriza_value)
comp.adicionarSeparador()

comp.exibirPergunta('Apresenta Dificuldade para Respirar (Dispneia)?')
dispneia_value = st.radio('id_dispneia', options=comp.radio_options,label_visibility='collapsed')
dispneia = comp.radio_values.get(dispneia_value)
comp.adicionarSeparador()

comp.exibirPergunta('Apresenta Tosse?')
tosse_value = st.radio('id_tosse', options=comp.radio_options,label_visibility='collapsed')
tosse = comp.radio_values.get(tosse_value)
comp.adicionarSeparador()

comp.exibirPergunta('Possui Diabetes?')
diabetes_value = st.radio('id_diabets', options=comp.radio_options,label_visibility='collapsed')
diabetes = comp.radio_values.get(diabetes_value)
comp.adicionarSeparador()

comp.exibirPergunta('Possui Problema Renal?')
renal_value = st.radio('id_renal', options=comp.radio_options,label_visibility='collapsed')
renal = comp.radio_values.get(renal_value)
comp.adicionarSeparador()

dados = {
    'faixaetaria': faixaetaria,
    'qntVacinas': qntVacinas,
    'faixaDiasSintomas': faixaDiasSintomas,
    'dorDeGarganta': dorDeGarganta,
    'dorDeCabeca': dorDeCabeca,
    'coriza': coriza,
    'dispneia': dispneia,
    'tosse': tosse,
    'diabetes': diabetes,
    'renal': renal,
}

modelo = md.importarModelo(modeloSelecionado)
botao = st.button('Efetuar Predição')
if(botao):
    # dadosFormatados = np.array([[dados]])
    dadosFormatados = pd.DataFrame([dados])
    resultado = modelo.predict_proba(dadosFormatados)
    probInternacao =  round(resultado[0][0] * 100, 3)
    comp.exibirProbabilidade(str(probInternacao))
    # st.write('Dados: ', dadosFormatados)
    
comp.adicionarSeparador()
comp.exibirFooter()