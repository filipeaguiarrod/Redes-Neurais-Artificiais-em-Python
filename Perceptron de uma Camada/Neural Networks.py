# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:43:58 2020

@author: rodri
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ConfusionMatrix
import numpy as np
from sklearn.metrics import confusion_matrix
### Instalar via cmd pip install tensorflow (framework google)
### Instalar via cmd pip install keras

from keras.models import Sequential
from keras.layers import Dense # Dense todos neuronios estão conectados 
# em todas camadas.
from keras.utils import np_utils

base = datasets.load_iris()
previsores = base.data
classe = base.target


#criando variavel binarizando os resultados
#pois deverão ter 3 neuronios - 1p/ cada classe
# para saber se ele é da classe 0   ativo neuronio 1 

classe_dummy = np_utils.to_categorical(classe)

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,classe_dummy,test_size = 0.3,random_state=0)

# Construção da Rede Neural - 1ºEstruturando

modelo=Sequential() # uma camada após a outra
#Adicionando primeira camada oculta c/ 5 neurônios
#Quantidade de neurônios de entrada = qtde de atributos previsores (4)
modelo.add(Dense(units=5,input_dim=4))
#intermediaria
# neurônios 4 que é a média de neurônios de entrada e saída
modelo.add(Dense(units=4))
#camada de saída.
#1 neurônio para cada classe (3) 
#softmax para quando tenho + 1 um classificador final
modelo.add(Dense(units=3,activation="softmax"))

modelo.summary()#resumo do modelo

# para plotar modelo visualmente
from keras.utils.vis_utils import plot_model

# Construção da Rede Neural - 2ºTreinando

#Adam - Algoritimo de atualização dos pesos (ajuste
#calculo do erro -loss - "categorical_crossentropy" problema com + de 2 classes
#metrics - accuracy - quero visualizar pela taxa de acerto

modelo.compile(optimizer ="adam",loss="categorical_crossentropy",metrics=["accuracy"])

#epochs quantas vezes rodar o algoritimo
modelo.fit(X_treinamento,y_treinamento,epochs=1000, validation_data=(X_teste,y_teste))

#val_accuracy é o quanto ele acertou baseado no teste


############## Previsões de teste

previsoes = modelo.predict(X_teste)

#retorna valores de probabilidade dentro do treinamento.

previsoes = (previsoes>0.5) # faz o teste lógico

############ Matriz de Confusão


y_teste_matrix=[np.argmax(t) for t in y_teste]
y_previsao_matrix = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matrix, y_previsao_matrix)

Acerto = (np.trace(confusao)/np.sum(confusao))*100

