import streamlit as st
import streamlit.components.v1 as components

# Definindo os Valores das Opções
radio_options = ['Sim', 'Não']
radio_values = {'Sim': 1, 'Não': 0}

vacinas_options = ['Nenhuma', '1 Dose', '2 Doses']
vacinas_values = {'Nenhuma': 0, '1 Dose': 1, '2 Doses': 2}

modelo_options = ['Gradient Boosting', 'Logistic Regression', 
                  'Random Forest', 'Ada Boost']

faixaetaria_options = ['0-11 Anos', '12-17 Anos', '18-29 Anos', 
                       '30-44 Anos', '45-59 Anos','60-74 Anos', 
                       '75-89 Anos', '> 90 Anos']
faixaetaria_values = {'0-11 Anos': 0, '12-17 Anos': 1, '18-29 Anos': 2, 
                      '30-44 Anos': 3, '45-59 Anos': 4, '60-74 Anos': 5, 
                      '75-89 Anos': 6, '> 90 Anos': 7}

faixaDiasSintomas_options = ['até 3 dias', '4 e 6 dias', '7 e 9 dias', 
                             '10 e 12 dias', '13 e 15 dias', '16 e 18 dias', 
                             'Mais de 18 dias']
faixaDiasSintomas_values = {'até 3 dias': 0, '4 e 6 dias': 1, '7 e 9 dias': 2, 
                            '10 e 12 dias': 3, '13 e 15 dias': 4, '16 e 18 dias': 5, 
                            'Mais de 18 dias': 6}


# Cabeçalho da Página
def cabecalhoPagina():
    return components.html("""<h3 style="text-align: center; font-family: sans-serif; color: white">
                           Programa de Pós-Graduação em Ciências da Computação - PPgCC
                           </h3>""", height=100)
    
# Adiciona uma linha de separação
def adicionarSeparador():
    return st.markdown("""---""")

# Exibir as Perguntas em h3
def exibirPergunta(conteudo):
    return components.html(
        """<h3 style="font-family: sans-serif; color: white">""" + conteudo + """</h3>""", height=40)
