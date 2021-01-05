# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:30:54 2020

@author: rodri
"""

# Otimizando Percpetron com numpy (soma)


import numpy as np

# Entrada e pesos

e = np.array([-1,7,5]) #np.array cria um array do numpy.
p=np.array([0.8,0.1,0])
    
# Simulando função soma do perceptron

def soma(e,p):
   return e.dot(p) # Comando dot (dot product/ produtor escalar)

#Testando 
s=soma(e,p)

#Criando a Step Function

def StepFunction(soma):
    if(soma>=1):
        return 1
    return 0

r=StepFunction(s)