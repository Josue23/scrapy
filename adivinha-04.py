
# coding: utf-8

# In[ ]:

numero = 50
chute = int(input('Digite um número: '))


# In[ ]:

# numero = 50
# chute = int(input('Digite um número: '))

tentativa = 1
while tentativa <= 5:
    if diferenca == 0:
        print('Você acertou!!')
        break
    diferenca = numero - chute
    if diferenca > 0:
        print('Você errou!!')
        print('Dica: O número que você procura é maior que %s.' %chute)
    else:
        print('Você errou!!')
        print('Dica: O número que você procura é menor que %s.' %chute)

    # verifica se está frio ou quente
    if abs(diferenca) <= abs(numero) * .2: # verifica se a diferença é menor que 20% da variável numero
        print('Está quente!!')
    else:
        print('Está frio!!')

    tentativa += 1
    chute = int(input('Tente novamente \nDigite um número: '))



# In[ ]:



