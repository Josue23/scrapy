#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=ilht0bsD0ks
algoritmos gulosos
    sempre escolhe a alternativa que parece mais promissora naquele instante
    nunca reconsidera essa decisão
    uma escolha que foi feita nunca é revista
    não há backtracking
    a escolha e feita de acordo com critério guloso - decisão localmente ótima
    nem sempre dão soluções ótimas

problema do troco (troco mínimo)
moedas = (100, 50, 25, 5, 1)

exemplo de etroco: 75 centavos
qual a qtde mínima de moedas?
2 moedas (1 moeda de 50, 1 moeda de 25)
'''

moedas = [100, 50, 25, 5, 1]
troco = int(input('Digite o valor do troco: '))
totalTroco = 0
moedas100 = 0
moedas50 = 0
moedas25 = 0
moedas5 = 0
moedas1 = 0

for moeda in moedas:
    if moeda <= abs(troco - totalTroco):
        moedas[moeda] += 1
        totalTroco += moeda

print('Quantidade mínima de moedas: %d ' %qtmoedas)