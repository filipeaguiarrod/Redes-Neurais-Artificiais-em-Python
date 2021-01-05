# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:16:09 2020

@author: rodri
"""

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist

# Carregando dados, sendo Y os classificadores
(X_treinamento, y_treinamento),(X_teste, y_teste) = mnist.load_data()

#visualizando números dentro da matriz
plt.imshow(X_treinamento[2],cmap="gray")
plt.title(y_treinamento[2])


#Mudando (60000,28,28) achatando para (60000,784)
#np.prod multiplica 28x28 i
X_treinamento = X_treinamento.reshape((len(X_treinamento), np.prod(X_treinamento.shape[1:])))
X_teste = X_teste.reshape((len(X_teste), np.prod(X_teste.shape[1:])))

#Converter os valores de X_teste e X_treinamento para float.
#Precisamos normalizar os dados em uma escala de 0 e 1

X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')

# por teste, usando valores inteiros ele tem uma performance baixa;
# dividiremos pelo maior valor da base 
#caso não estivesse em float ele não ia conseguir dividir a base
# valores menores, mais rápido o algoritimo

X_treinamento /= 255
X_teste /= 255

# Precisamos criar variáveis do tipo Dummy binarizar os classificadores;
# 10 classes 0 a 9 ( exclui o maiorX_treinamento /= 255)

y_treinamento = np_utils.to_categorical(y_treinamento,10)
y_teste = np_utils.to_categorical(y_teste,10)

########################## Criação da Rede Neural

modelo=Sequential() # São sequência de camadas ao qual vou add cada.

#Adicionando primeira camada escondida
# função relu tem sido legal para deep learning imagem
#input_dim é só na primeira camada
modelo.add(Dense(units=64,activation="relu",input_dim = 784))
#camada dropout serve para zerar entradas em muitos neuronios de entrada
#evita o overfiting no treinamento,
# dos 64 neurônios ele zera 20%
modelo.add(Dropout(0.2))
modelo.add(Dense(units=64,activation="relu"))
modelo.add(Dropout(0.2))
modelo.add(Dense(units=64,activation="relu"))
modelo.add(Dropout(0.2))
# Se conecta na cama de saída:
# 10 possíveis saídas
#softmax retorna uma probabilidade de ser uma classificador;
modelo.add(Dense(units=10,activation="softmax"))


#VIsualizar a construção:

modelo.summary()

#Adam - Algoritimo de atualização dos pesos (ajuste)
#calculo do erro -loss - "categorical_crossentropy" problema com + de 2 classes
#metrics - accuracy - quero visualizar pela taxa de acerto

modelo.compile(optimizer ="adam",loss="categorical_crossentropy",metrics=["accuracy"])

#Treinamento
historico = modelo.fit(X_treinamento,y_treinamento,epochs =20,validation_data=[X_teste,y_teste] )

historico.history.keys()

#val_accuracy = acerto de acordo com base de dados de teste
#loss = erro

plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_accuracy'])

previsoes = modelo.predict(X_teste)

#retorna valores de probabilidade dentro do treinamento.

previsoes = (previsoes>0.5) # faz o teste lógico

############ Matriz de Confusão


y_teste_matrix=[np.argmax(t) for t in y_teste]
y_previsao_matrix = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matrix, y_previsao_matrix)

Acerto = (np.trace(confusao)/np.sum(confusao))*100


############# PRevendo através do modelo criado

y_treinamento[20] # 4 
X_treinamento[20]

novo = X_treinamento[20]
novo=np.expand_dims(novo,axis=0)
pred = modelo.predict(novo)