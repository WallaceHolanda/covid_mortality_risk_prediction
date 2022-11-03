from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

import streamlit as st
import joblib
import sklearn
import numpy as np
import pandas as pd
import os


def criarModelo(modelo, baseObitoCurado, alvo):
    x_train, x_test, y_train, y_test = train_test_split(baseObitoCurado.drop(alvo, axis=1),
                                                        baseObitoCurado[alvo],
                                                        test_size=0.3,
                                                        random_state=42)

    modeloClassificador = modelo
    modeloClassificador.fit(x_train, y_train)
    return modeloClassificador


def importarModelo(modeloEscolhido):
    url = 'streamlit/predicao_internacao/bases/ba-ic-7030-sp.xlsx'
    alvo = 'evolucaoCaso'
    baseObitoCurado = pd.read_excel(url, engine="openpyxl")
    
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
    
    atributosSelecionados = ['faixaetaria', 'qntVacinas', 'faixaDiasSintomas', 
                             'dorDeCabeca', 'dorDeGarganta', 'coriza', 
                             'dispneia', 'tosse', 'diabetes', 'renal', 'evolucaoCaso']

    baseObitoCurado = baseObitoCurado.loc[:, atributosSelecionados]

    return criarModelo(modeloEscolhido, baseObitoCurado, alvo)


modeloAB = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
                              learning_rate=1.0, n_estimators=50, random_state=410)

modeloRF = RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                                  criterion='gini', max_depth=None, max_features='auto',
                                  max_leaf_nodes=None, max_samples=None,
                                  min_impurity_decrease=0.0,
                                  min_samples_leaf=1, min_samples_split=2,
                                  min_weight_fraction_leaf=0.0, n_estimators=100,
                                  n_jobs=-1, oob_score=False, random_state=7374, verbose=0,
                                  warm_start=False)

modeloLR = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                              intercept_scaling=1, l1_ratio=None, max_iter=1000, multi_class='auto',
                              n_jobs=None, penalty='l2', random_state=1340, solver='lbfgs',
                              tol=0.0001, verbose=0, warm_start=False)

modeloGB = GradientBoostingClassifier(ccp_alpha=0.0, criterion='friedman_mse', init=None,
                           learning_rate=0.1, loss='deviance', max_depth=3,
                           max_features=None, max_leaf_nodes=None,
                           min_impurity_decrease=0.0,
                           min_samples_leaf=1, min_samples_split=2,
                           min_weight_fraction_leaf=0.0, n_estimators=100,
                           n_iter_no_change=None, 
                           random_state=1859, subsample=1.0, tol=0.0001,
                           validation_fraction=0.1, verbose=0,
                           warm_start=False)


# Definindo os Valores das Opções
radio_options = ['Sim', 'Não']
radio_values = {'Sim': 1, 'Não': 0}

vacinas_options = ['Nenhuma', '1 Dose', '2 Doses']
vacinas_values = {'Nenhuma': 0, '1 Dose': 1, '2 Doses': 2}

modelo_options = ['Gradient Boosting', 'Logistic Regression', 'Random Forest', 'Ada Boost']

modelo_values = {'Gradient Boosting': modeloGB, 'Random Forest': modeloRF, 
                 'Logistic Regression': modeloLR, 'Ada Boost': modeloAB}

faixaetaria_options = ['0-11 Anos', '12-17 Anos', '18-29 Anos', '30-44 Anos', '45-59 Anos',
                       '60-74 Anos', '75-89 Anos', '> 90 Anos']

faixaetaria_values = {'0-11 Anos': 0, '12-17 Anos': 1, '18-29 Anos': 2, '30-44 Anos': 3,
                      '45-59 Anos': 4, '60-74 Anos': 5, '75-89 Anos': 6, '> 90 Anos': 7}

faixaDiasSintomas_options = ['até 3 dias', '4 e 6 dias', '7 e 9 dias', '10 e 12 dias',
                        '13 e 15 dias', '16 e 18 dias', 'Mais de 18 dias']

faixaDiasSintomas_values = {'até 3 dias': 0, '4 e 6 dias': 1, '7 e 9 dias': 2, '10 e 12 dias': 3,
                        '13 e 15 dias': 4, '16 e 18 dias': 5, 'Mais de 18 dias': 6}

st.header('Modelo de Predição do Risco de Internação')
st.subheader(
    'Preencha as solicitadas solicitadas para obter a probabilidade do risco de agravamento:')

# Definindo os campos de entrada
modelo_value = st.selectbox('Escolha o Modelo', options=modelo_options)
modeloSelecionado = modelo_values.get(modelo_value)

faixaetaria_value = st.radio(
    'Qual a sua faixa-etária?', options=faixaetaria_options)
faixaetaria = faixaetaria_values.get(faixaetaria_value)

qntVacinas_value = st.radio(
    'Quantas doses da vacina você tomou?', options=vacinas_options)
qntVacinas = vacinas_values.get(qntVacinas_value)

faixaDiasSintomas_value = st.radio(
    'Quantos dias se passaram desde o primeiro sintoma?', options=faixaDiasSintomas_options)
faixaDiasSintomas = faixaDiasSintomas_values.get(faixaDiasSintomas_value)

dorDeGarganta_value = st.radio(
    'Apresenta Dor de Garganta?', options=radio_options)
dorDeGarganta = radio_values.get(dorDeGarganta_value)

dorDeCabeca_value = st.radio('Apresenta Dor de Cabeça?', options=radio_options)
dorDeCabeca = radio_values.get(dorDeCabeca_value)

coriza_value = st.radio('Apresenta Coriza?', options=radio_options)
coriza = radio_values.get(coriza_value)

dispneia_value = st.radio('Apresenta Dificuldade para Respirar (Dispneia)?', options=radio_options)
dispneia = radio_values.get(dispneia_value)

tosse_value = st.radio('Apresenta Tosse?', options=radio_options)
tosse = radio_values.get(tosse_value)

diabetes_value = st.radio('Possui Diabetes?', options=radio_options)
diabetes = radio_values.get(diabetes_value)

renal_value = st.radio('Possui Problema Renal?', options=radio_options)
renal = radio_values.get(renal_value)

# st.write(dorDeCabeca, cardica)


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

modelo = importarModelo(modeloSelecionado)
botao = st.button('Efetuar Predição')
if(botao):
    # dadosFormatados = np.array([[dados]])
    dadosFormatados = pd.DataFrame([dados])
    resultado = modelo.predict_proba(dadosFormatados)
    probInternacao =  round(resultado[0][0] * 100, 3)
    st.write('Probabilidade de Internacao: ', probInternacao, ' %')
    # st.write('Dados: ', dadosFormatados)
