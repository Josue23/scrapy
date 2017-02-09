import random
continua = True

############     connstrói a função que sorteia as faces de cada dado       ############
def sorteia_numeros(faces):
    dados = int(input('Número de dados: '))
    for dado in range(dados): # range gera uma LISTA de 0 até número de dados menos 1
        numero = random.randint(1, faces)
        print('%2dº dado: %2d ' %(dado+1, numero))

while continua:
    faces = input('\nPressione a tecla ESPAÇO para parar ou \nDigite um número de faces: ')
    #if faces == "parar":
    if faces == chr(32): # tecla space
        continua = False # the loop stops
    else:
        faces = int(faces)
        sorteia_numeros(faces)  #  chama a função sorteia_numeros
print("Fim do programa!!")
