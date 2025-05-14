import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Carrega modelos
modelo_linear = pickle.load(open('modelo/modelo_linear.pkl', 'rb'))
modelo_arvore = pickle.load(open('modelo/modelo_arvore.pkl', 'rb'))
modelo_knn = pickle.load(open('modelo/modelo_knn.pkl', 'rb'))
modelo_rede_neural = load_model('modelo/modelo_rede_neural.h5')

def prever_preco(entrada, modelo_nome):
    entrada_np = np.array([entrada])
    if modelo_nome == 'linear':
        return modelo_linear.predict(entrada_np)[0]
    elif modelo_nome == 'arvore':
        return modelo_arvore.predict(entrada_np)[0]
    elif modelo_nome == 'knn':
        return modelo_knn.predict(entrada_np)[0]
    elif modelo_nome == 'rede_neural':
        return modelo_rede_neural.predict(entrada_np)[0][0]
    else:
        return 'Modelo não reconhecido.'
