from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

import sklearn
import numpy as np
import pandas as pd

# Divide a base de dados e realiza o fit a partir do modelo especificado
def __criarModelo__(modelo, baseObitoCurado, alvo):
    x_train, x_test, y_train, y_test = train_test_split(baseObitoCurado.drop(alvo, axis=1),
                                                        baseObitoCurado[alvo],
                                                        test_size=0.3,
                                                        random_state=42)
    modeloClassificador = modelo
    modeloClassificador.fit(x_train, y_train)
    return modeloClassificador

# Carrega os dados da base, em seguida cria e retorna o modelo
def importarModelo(modeloEscolhido):
    url = 'streamlit/predicao_internacao/bases/ba-ic-7030-sp.xlsx'
    alvo = 'evolucaoCaso'
    baseObitoCurado = pd.read_excel(url, engine="openpyxl")
    atributosSelecionados = ['faixaetaria', 'qntVacinas', 'faixaDiasSintomas', 
                             'dorDeCabeca', 'dorDeGarganta', 'coriza', 
                             'dispneia', 'tosse', 'diabetes', 'renal', 'evolucaoCaso']
    baseObitoCurado = baseObitoCurado.loc[:, atributosSelecionados]
    return __criarModelo__(modeloEscolhido, baseObitoCurado, alvo)

def criaAdaBoost():
    return AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
                              learning_rate=1.0, n_estimators=50, random_state=410)

def criaRandomForest():
    return RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                                criterion='gini', max_depth=None, max_features='auto',
                                max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0,
                                min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, 
                                n_estimators=100, n_jobs=-1, oob_score=False, random_state=7374, 
                                verbose=0, warm_start=False)

def criaLogisticRegression():
    return LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                              intercept_scaling=1, l1_ratio=None, max_iter=1000, multi_class='auto',
                              n_jobs=None, penalty='l2', random_state=1340, solver='lbfgs',
                              tol=0.0001, verbose=0, warm_start=False)
    
def criaGradientBoosting():    
    return GradientBoostingClassifier(ccp_alpha=0.0, criterion='friedman_mse', init=None,
                           learning_rate=0.1, loss='deviance', max_depth=3,
                           max_features=None, max_leaf_nodes=None,
                           min_impurity_decrease=0.0,
                           min_samples_leaf=1, min_samples_split=2,
                           min_weight_fraction_leaf=0.0, n_estimators=100,
                           n_iter_no_change=None, 
                           random_state=1859, subsample=1.0, tol=0.0001,
                           validation_fraction=0.1, verbose=0,
                           warm_start=False)
