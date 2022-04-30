from listplayers import seleciona
from newplayer import newplayer
from util import clear
from dbinit import initDB

initDB()

option = '1'

while (option != '0'):
    clear()

    contador = 1

    while (contador != 86):
        if (contador <= 41):
            print('*', end=" ")
        elif (contador == 42):
            print()
        elif (contador  == 43):
            print('*         ', end=" ")
            print('Bem vindo ao MuD - Star Wars. Que a Força esteja com você!', end=" ")
            print('          *')
        elif (contador <= 84):
            print('*', end=" ")
        else:
            print('\n')
        
        contador = contador + 1

    if (option != '1' and option != '2' and option != '0'):
        print('Opção Inválida! =( \n')

    print('Como deseja jogar?')
    print('''
          [1] Começar com um novo jogador
          [2] Continuar com um jogador existente
          [0] Sair do jogo
          ''')
    option = str(input('Escolha uma opção: '))
    if (option != '1' and option != '2'):
        continue
    elif (option == '1'):
        newplayer()
    else:
        seleciona()

contador = 1

clear()

while (contador != 85):
    if (contador <= 41):
        print('*', end=" ")
    elif (contador == 42):
        print()
    elif (contador  == 43):
        print('*                              ', end=" ")
        print('Você saiu do jogo.', end=" ")
        print('                             *')
        print('*         E, lembre-se: "A habilidade de falar não o torna inteligente"', end=" ")
        print('        *')
    else:
        print('*', end=" ")
       
    contador = contador + 1

print()
