# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:14:54 2020

@author: rodri
"""

# Entrada e pesos

e = [-1,7,5]
p=[0.8,0.1,0]
    
# Simulando função soma do perceptron

def soma(e,p):
    s=0
    for i in range(len(e)):
        #print(e[i])
        #print(p[i])
        s += e[i]*p[i]
    return s

#Testando 
s=soma(e,p)

#Criando a Step Function

def StepFunction(soma):
    if(soma>=1):
        return 1
    return 0

r=StepFunction(s)