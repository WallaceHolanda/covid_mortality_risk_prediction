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
    url = 'streamlit/bases/oc-vacina-6040-sp.xlsx'
    alvo = 'evolucaoCaso'
    baseObitoCurado = pd.read_excel(url)

    atributosSelecionados = ['faixaetaria', 'dispneia', 'qntVacinas', 'dorDeGarganta',
                             'coriza', 'diabetes', 'dorDeCabeca', 'cardiaca', 'evolucaoCaso']

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
                                      random_state=2333, subsample=1.0, tol=0.0001,
                                      validation_fraction=0.1, verbose=0,
                                      warm_start=False)


# Definindo os Valores das Opções
radio_options = ['Sim', 'Não']
radio_values = {'Sim': 1, 'Não': 0}

vacinas_options = ['Nenhuma', '1 Dose', '2 Doses']
vacinas_values = {'Nenhuma': 0, '1 Dose': 1, '2 Doses': 2}


modelo_options = ['Logistic Regression', 'Random Forest', 'Gradient Boosting', 'Ada Boost']

modelo_values = {'Random Forest': modeloRF, 'Gradient Boosting': modeloGB,
                 'Logistic Regression': modeloLR, 'Ada Boost': modeloAB}

faixaetaria_options = ['0-11 Anos', '12-17 Anos', '18-29 Anos', '30-44 Anos', '45-59 Anos',
                       '60-74 Anos', '75-89 Anos', '> 90 Anos']

faixaetaria_values = {'0-11 Anos': 0, '12-17 Anos': 1, '18-29 Anos': 2, '30-44 Anos': 3,
                      '45-59 Anos': 4, '60-74 Anos': 5, '75-89 Anos': 6, '> 90 Anos': 7}


st.header('Modelo Óbito-Curado')
st.subheader(
    'Preencha as seguintes informações para obter a predição de agravamento.')

# Definindo os campos de entrada
modelo_value = st.selectbox('Escolha o Modelo', options=modelo_options)
modeloSelecionado = modelo_values.get(modelo_value)

faixaetaria_value = st.radio(
    'Qual a sua faixa-etária?', options=faixaetaria_options)
faixaetaria = faixaetaria_values.get(faixaetaria_value)

qntVacinas_value = st.radio(
    'Quantas doses da vacina você tomou?', options=vacinas_options)
qntVacinas = vacinas_values.get(qntVacinas_value)

dorDeGarganta_value = st.radio(
    'Possui Dor de Garganta?', options=radio_options)
dorDeGarganta = radio_values.get(dorDeGarganta_value)

dispneia_value = st.radio('Possui Dispnéia?', options=radio_options)
dispneia = radio_values.get(dispneia_value)

coriza_value = st.radio('Possui Coriza?', options=radio_options)
coriza = radio_values.get(coriza_value)

dorDeCabeca_value = st.radio('Possui Dor de Cabeça?', options=radio_options)
dorDeCabeca = radio_values.get(dorDeCabeca_value)

diabetes_value = st.radio('Possui Diabetes?', options=radio_options)
diabetes = radio_values.get(diabetes_value)

cardiaca_value = st.radio('Possui Problema Cardíaco?', options=radio_options)
cardiaca = radio_values.get(cardiaca_value)

# st.write(dorDeCabeca, cardica)

dados = {
    'faixaetaria': faixaetaria,
    'qntVacinas': qntVacinas,
    'dorDeGarganta': dorDeGarganta,
    'dorDeCabeca': dorDeCabeca,
    'coriza': coriza,
    'dispneia': dispneia,
    'diabetes': diabetes,
    'cardiaca': cardiaca,
}

# dados = [faixaetaria, qntVacinas, dorDeGarganta, dorDeCabeca,
#          coriza, dispneia, diabetes, cardiaca]


modelo = importarModelo(modeloSelecionado)
botao = st.button('Efetuar Predição')
if(botao):
    # dadosFormatados = np.array([[dados]])
    dadosFormatados = pd.DataFrame([dados])
    resultado = modelo.predict_proba(dadosFormatados)
    probAgravamento =  round(resultado[0][0] * 100, 3)
    st.write('Probabilidade de Agravamento: ', probAgravamento, ' %')
    # st.write('Dados: ', dadosFormatados)
