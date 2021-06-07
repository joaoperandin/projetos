import random

maiuscula1=chr(random.randint(65,90)) #cria uma letra maiúscula aleatória baseada em código ASCII
maiuscula2=chr(random.randint(65,90)) 

minuscula1=chr(random.randint(97,122)) #cria uma letra minuscula aleatória baseada em código ASCII
minuscula2=chr(random.randint(97,122))

digito1=random.randint(0,9) #cria um número aleatório entre 0 e 9
digito2=random.randint(0,9)

especial1=chr(random.randint(33,38))#cria um caractére especial baseada em código ASCII
especial2=chr(random.randint(33,38))

lista = [maiuscula1,maiuscula2,minuscula1,minuscula2,digito1,digito2,especial1,especial2] #lista com todos as variáveis incluídas na senha.

random.shuffle(lista) #para embaralhar os caractéres

usuario1 = False #arrumando um loop para criar outras senhas

while usuario1 == False:
    usuario = input('Você quer gerar uma senha aleatória? Digite Y para sim e N para não.\n')
    if usuario == 'Y' or usuario == 'y':
        print('Sua senha é:')
        print(*lista, sep='')#comando pra imprimir a lista toda junta
        usuario1 = True #arrumando para o próximo loop//criar outra senha
    if usuario1 == True:
        escolha = input('Deseja criar outra senha? Y = sim / N = não.\n')
        if escolha == 'Y' or escolha == 'y':
            usuario1 = False #volta para o primeiro loop
        elif escolha == 'N' or escolha == 'n':
            print('Ok. Finalizando programa...')
            break
        else:
            usuario1 = False #volta para o primeiro loop
            print('Por favor, escolha Y ou N.')
    elif usuario == 'N' or usuario == 'n':
        print('Ok. Finalizando programa...')
        break
    else:
        print('Por favor, escolha Y ou N.')
