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

problema do troco (troco mínimo em moedas)
moedas = (100, 50, 25, 5, 1)

exemplo de troco:
75 centavos
qual a qtde mínima de moedas?
2 moedas (1 moeda de 50, 1 moeda de 25)
'''

moedas = [100, 50, 25, 5, 1]
qtdMoedas = 0
troco = int(input('Digite o troco: '))

for i in range(len(moedas)):
    num_moedas = troco // moedas[i]
    troco -= num_moedas * moedas[i]
    qtdMoedas += num_moedas

    if troco == 0:
        break

print('Qtd de moedas: %d ' %qtdMoedas)