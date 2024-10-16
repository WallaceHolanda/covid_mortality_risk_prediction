import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

# Textos Utilizados
titulo = "Risk of Hospitalization Prediction"
descricao = """This Prediction Model is the result of the dissertation work of the Postgraduate Program
in Computer Science (PPgCC) carried out by Wallace Duarte de Holanda, under the supervision of
Prof. Dr. Lenardo Chaves e Silva."""
comoUsar = """To make a Hospitalization Prediction, first choose your preferred Model and then answer
the set of questions about your health status."""
aProbabilidadeEh = "The probability of hospitalization is "
copyright = "Copyright © 2023 - "

# Definindo os Valores das Opções
radio_options = ['Yes', 'No']
radio_values = {'Yes': 1, 'No': 0}

vacinas_options = ['None', '1 Dose', '2 Doses']
vacinas_values = {'None': 0, '1 Dose': 1, '2 Doses': 2}

modelo_options = ['Gradient Boosting', 'Logistic Regression', 
                  'Random Forest', 'Ada Boost']

faixaetaria_options = ['0-11 years', '12-17 years', '18-29 years', 
                       '30-44 years', '45-59 years','60-74 years', 
                       '75-89 years', 'Over 90 years']
faixaetaria_values = {'0-11 years': 0, '12-17 years': 1, '18-29 years': 2, 
                      '30-44 years': 3, '45-59 years': 4, '60-74 years': 5, 
                      '75-89 years': 6, 'Over 90 years': 7}

faixaDiasSintomas_options = ['up to 3 days', '4 to 6 days', '7 to 9 days', 
                             '10 to 12 days', '13 to 15 days', '16 to 18 days', 
                             'More than 18 days']
faixaDiasSintomas_values = {'up to 3 days': 0, '4 to 6 days': 1, '7 to 9 days': 2, 
                            '10 to 12 days': 3, '13 to 15 days': 4, '16 to 18 days': 5, 
                            'More than 18 days': 6}

# Exibir imagem do cabeçalho
def imagemCabecalho():
    col1, col2, col3 = st.columns([2,6,2])
    with col2:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(diretorio_atual, 'images', 'logos.png')
        logomarcas = Image.open(caminho_imagem)
        st.image(logomarcas, use_column_width = 'auto')

# Cabeçalho da Página
def cabecalhoPagina():
    return components.html("""<h1 style="text-align: center; font-family: sans-serif; color: white">
                           """ + titulo + """</h1>
                           <h4 style="font-weight: 500; text-align: justify; font-family: sans-serif; color: white; line-height: 1.45">""" 
                           + descricao +
                           """</h4>
                           <h4 style="font-weight: 500; text-align: justify; font-family: sans-serif; color: white; line-height: 1.45">""" 
                           + comoUsar +
                           """</h4>
                           <br>
                           <hr size="5" width="90%" color="##BCF4BC">
                           """, height=300)
    
# Adiciona uma linha de separação
def adicionarSeparador():
    return st.markdown("""---""")

# Exibir as Perguntas em h3
def exibirPergunta(conteudo):
    return components.html(
        """<h3 style="text-align: left; font-family: sans-serif; color: white">""" + conteudo + """</h3>""", height=40)

def exibirProbabilidade(probabilidade):
    return components.html("""<p style="font-family: sans-serif; color: white">"""+ aProbabilidadeEh +
                           """<strong>""" + probabilidade + """</strong>"""
                           """% </p>""", height=40)

def exibirFooter():
    return components.html(""" <footer style="text-align: center; font-family: sans-serif; color: white">
                           """ + copyright + """
                           <a href="mailto:wallace.holanda@alunos.ufersa.edu.br" style="color: lightblue;">Contact</a>
                           </footer>""")