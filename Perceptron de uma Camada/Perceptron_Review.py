# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:14:37 2020

@author: rodri
"""

# Entrada e pesos para matriz: OR
# x1 x2 sáidas
# 0 0 0
# 0 1 1 
# 1 0 1 
# 1 1 1

#entradas = np.array([[0,0],[0,1],[1,0],[1,1]]) #np.array cria um array do numpy.
#saída = np.array([0,1,1,1]) # Resultado Esperado (Supervisionado)

# Entrada e pesos para matriz: XOR
# x1 x2 sáidas
# 0 0 0
# 0 1 1 
# 1 0 1 
# 1 1 1

#entradas = np.array([[0,0],[0,1],[1,0],[1,1]]) #np.array cria um array do numpy.
#saída = np.array([0,1,1,0]) # Resultado Esperado (Supervisionado)



import numpy as np

# Entrada e pesos para matriz: AND
# x1 x2 sáidas
# 0 0 0
# 0 1 0 
# 1 0 0 
# 1 1 1


entradas = np.array([[0,0],[0,1],[1,0],[1,1]]) #np.array cria um array do numpy.
saída = np.array([0,0,0,1]) # Resultado Esperado (Supervisionado)





#Criando um script para rodar o Perceptron:

pesos = np.array([0.0,0.0]) #valores pequenos colocar ponto se não ele arredonda
ta = 0.1 # taxa de aprendizagem   
erro = 1 # responsável por dizer se existe erro no step executado
erroTotal = 1 # conta os erros totais no ciclo ( 4 ciclos, por linha)

# soma dos steps:

while (erroTotal!=0):
    
    erroTotal = 0 # Apenas para iniciar o contador.    
    
    
    output = entradas.dot(pesos) # calcula por produto vetorial a saída
    output_calc = np.where(output>=1,1,0) # teste lógico (step function) para ativação ou nao!
    
    
    
    for i in range(len(output_calc)):
        erro = saída[i]-output_calc[i] # Calcula o erro em cada linha do Output com saída / posso colocar abs
        print("Erro local", erro) # imprime o erro para cada linha
        erroTotal += erro # depois de passar por todas as linhas ele me fala no final qual peso total. Quero conseguir prever 100%
        
        
        for j in range(len(pesos)): #Atualiza pesos mesmo com valor de erro zero ! para cada linha e cada coluna 
            pesos[j] = pesos[j] + (ta*entradas[i][j]*erro) # Atualiza pesos para cada entrada em cada linha
            print(round(pesos[j],2))
    
    print("Erro Total", erroTotal)

print("Os pesos otimizados", pesos)
    

        