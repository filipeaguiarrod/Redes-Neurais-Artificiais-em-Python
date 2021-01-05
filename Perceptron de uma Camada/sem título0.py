# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:14:13 2020

@author: rodri
"""

#Vamos precisar importar um módulo gerador de números inteiros aleatórios
from random import randint

#vamos criar um limite para a quantidade de jogos gerados
quant = 7

#vamos manter a estrutura do exercício anterior
seis_numeros = []

#precisamos criar uma lista vazia chamada (jogos) para receber as listas de 6 números
jogos = []

#para criar um novo contador que vai interromper o novo loop infinito, tornando a afirmação falsa
tot = 0

#esse é o loop que vai repetir tudo o que fizemos. Vamos usar o iterador condicional while
while tot <= quant:
    
#------------------
# para isso acontecer, vamos ter que indentar todo esse loop com o contador (linha tracejada)
# selecione tudo entre as linhas tracejadas e aperte (Tab)
    contador = 0 
    while True:
        num = randint(1, 60)
        if num not in seis_numeros:
            seis_numeros.append(num)
            contador += 1
        if contador == 6:
            #quebrando o loop infinito
            break    
    seis_numeros.sort()
#-------------------
    
    ###Agora podemos continuar...
    #vamos copiar todos os elementos da lista com 6 números para dentro da lista jogos
    jogos.append(seis_numeros[:])
    
    #uma vez que copiamos os números podemos limpar a lista para receber 6 novos números
    seis_numeros.clear()
    
    #por fim podemos contabilizar um novo jogo e começar tudo de novo
    tot +=1
    
#existe um último tipo de loop... ele é muito comum para dicionários
#mas também pode ser usado em listas iterando sobre seus indices e seus elementos.
for i, j in enumerate(jogos):
    print('jogo index:', i, ' lista com o jogo: ', j)