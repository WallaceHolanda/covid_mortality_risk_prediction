import numpy as np
import os
from flask import Flask, jsonify, request, jsonify
import pickle

## __name__ é definido por padrão. Poderiamos usar outra string qualquer aqui, porém,
## não recomendo, pois, isso poderia causar problemas em aplicações maiores.
app = Flask(__name__)

## carregando o modelo para o código
with open("./notebook/model.pickle","rb") as f:
    #Carrega o arquivo model.pickle em modo read binary
    meu_modelo = pickle.load(f)

# definimos aqui uma rota, no caso criamos a rota localhost:5000/
@app.route("/test")
def primeiro_endpoint_get():
  return ("Tudo Funcionando Corretamente !", 200) 

@app.route("/segundo_endpoint")
def segundo_endpoint():
  return ("Já criamos 2 funções !!", 200)

@app.route('/predict', methods=['POST'])
def predict():
  dados = request.get_json(force=True)
  predicao = meu_modelo.predict(np.array([list(dados.values())]))
  resultado = predicao[0]

  resposta = {'Possibilidade de Agravamento': bool(resultado)}
  return jsonify(resposta)

if __name__ == "__main__":
  debug = True # com essa opção como True, ao salvar, o "site" recarrega automaticamente.
  app.run(host='0.0.0.0', port=5000, debug=debug)
