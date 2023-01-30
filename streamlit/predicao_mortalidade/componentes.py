import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Textos Utilizados
titulo = "Predição do Risco de Mortalidade"
descricao = """Este Modelo de Predição é resultado do trabalho de Dissertação do Programa de Pós-Graduação
em Ciências da Computação (PPgCC) realizado por Wallace Duarte de Holanda, com orientação do Prof. 
Dr. Lenardo Chaves e Silva."""
comoUsar = """Para realizar a Predição da Mortalidade, inicialmente, escolha o Modelo de sua preferência, 
e em seguida responda o conjunto de perguntas sobre o seu estado de saúde."""
aProbabilidadeEh = "A Probabilidade de Mortalidade é de "
copyright = "Copyright © 2023 - "

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

# Exibir imagem do cabeçalho
def imagemCabecalho():
    col1, col2, col3 = st.columns([2,6,2])
    with col2:
        logomarcas = Image.open('streamlit/images/logos.png')
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
                           """% </p>""", height=30)

def exibirFooter():
    return components.html(""" <footer style="text-align: center; font-family: sans-serif; color: white">
                           """ + copyright + """
                           <a href="mailto:wallace.holanda@alunos.ufersa.edu.br" style="color: lightblue;">Contato</a>
                           </footer>""")