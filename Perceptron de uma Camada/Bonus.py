# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:14:24 2020

@author: rodri
"""

import pandas as pd
import numpy as np
dataset = pd.read_csv("Credit2.csv",sep=";")

# Separar variaveis dependentes das independentes / Class
# Transformar dados qualitativos pra numérico
# Binarizar resultado de classe


X = dataset.iloc[:,1:10].values # porém ele ignora o upper interval
y = dataset.iloc[:,10].values # sem range ele nao ignora linha

# tansformar categórico para valores / encoder:

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])

# Vai binarizar os dados.
# Estudar onehotencoder para diferenciar.
onehotencoder = make_column_transformer((OneHotEncoder(categories="auto",sparse=False),[1]),remainder='passthrough')
X = onehotencoder.fit_transform(X)

X = X[:,1:] # excluo uma coluna (1º)

# Ajuste dos classificadores

labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

# Binarizar resultados da classe para usar no keras.
from keras.utils import np_utils
classe_dummy = np_utils.to_categorical(y)


from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X,y,test_size = 0.2,random_state=0)

from sklearn.preprocessing import StandardScaler

# Padronização dos dados usando método Z-score
# Padroniza em relação a média zero e desvio padrão = 1
# trabalhar com números grandes, sobrecarrega processamento e tira eficiência
sc=StandardScaler()
X_treinamento = sc.fit_transform(X_treinamento)
X_teste = sc.fit_transform(X_teste)

# Criando rede neural artificial.
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential() # RNA do tipo sequêncial
# 6 neurônios na camada oculta
# 12  neurônios de entrada
classifier.add(Dense(units=6,kernel_initializer="uniform",activation = "relu",input_dim=12))
classifier.add(Dense(units=6,kernel_initializer="uniform",activation = "relu"))
classifier.add(Dense(units=1,kernel_initializer="uniform",activation = "sigmoid"))
classifier.compile(optimizer='adam', loss='binary_crossentropy',metrics=["accuracy"])
classifier.fit(X_treinamento,y_treinamento,batch_size=10,epochs=100)

classifier.summary()

y_pred = classifier.predict(X_teste)
y_pred = (y_pred>0.5)


from sklearn.metrics import confusion_matrix
confusao = confusion_matrix(y_teste, y_pred)

Acerto = (np.trace(confusao)/np.sum(confusao))*100