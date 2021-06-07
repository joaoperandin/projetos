print('*************************************************************\n                   PEDRA, PAPEL OU TESOURA\n *************************************************************')
from random import randint
#lista de opções
opcoes = ['pedra', 'papel', 'tesoura']

#fazendo o computador escolher uma das 3 opções na lista
cpu = opcoes[randint(0,2)]

#colocar jogador como False
player = False

while player == False:
#colocando jogador como True
    player = input('Escolha: pedra, papel ou tesoura: ')
    if player == cpu:
        print(f'O adversário também jogou {player}, empatou!')
    elif player == 'pedra':
        if cpu == 'papel':
            print('Seu adversário jogou papel!')
            print('Você perdeu!', cpu, 'ganha de', player,'!')
        else:
            print('Seu adversário jogou tesoura!') 
            print('Você ganhou!', player, 'ganha de', cpu,'!')
    elif player == 'papel':
        if cpu == 'tesoura':
            print('Seu adversário jogou tesoura!') 
            print('Você perdeu!', cpu, 'ganha de', player,'!')
        else:
            print('Seu adversário jogou pedra!') 
            print('Você ganhou!', player, 'ganha de', cpu,'!')
    elif player == 'tesoura':
        if cpu == 'pedra':
            print('Seu adversário jogou pedra!')
            print('Você perdeu!', cpu, 'ganha de', player,'!')
        else:
            print('Seu adversário jogou papel!')
            print('Você ganhou!', player, 'ganha de', cpu,'!')
    else:
        print('Essa palavra não é válida! Escreva uma das três opções.')
    
#o player tem que ficar como False para o loop continuar
    player = False
    cpu = opcoes[randint(0,2)]
