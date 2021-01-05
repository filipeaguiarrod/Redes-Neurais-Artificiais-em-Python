# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:14:10 2020

@author: rodri
"""


#Otimizando Percpetron com numpy (soma)


import numpy as np

# Entrada e pesos para matriz:
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
erroTot = 1

while (erroTot != 0): # Aqui defino que meu modelo tem de acertar 100%
        # cálculo soma
        #x1*p1+x2*p2 p/ cada linha
    soma = entradas.dot(pesos) # a saída de cada linha pelos pesos
    
    soma_bool = np.where(soma>=1,1,0) # função de ativação (saída calculada) retorna 1 ou zero
    
    erro = saída - soma_bool # Vetor de Erro
    
    for i in range(len(saída)): # erro total
        erroTot = 0
        erroTot += saída[i]-soma_bool[i]
        #print(erro)
    for j in range(len(pesos)):
        #print(j)
        pesos[j]=pesos[j]+(ta*entradas[i][j]*erro) #[j][i] localizando especificamente na entrada X1 e X2 da linha de erro máximo
    print(pesos)
        
print("Os pesos otimizados são: ",pesos)

