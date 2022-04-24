from listplayers import seleciona
from newplayer import newplayer


print('Bem vindo ao MuD - Star Wars. Que a Força esteja com você!')

option = 1

while (option != '0'):
    print('Como deseja jogar?')
    print('''
          [1] Começar com um novo jogador
          [2] Continuar com um jogador existente
          [0] Sair do jogo
          ''')
    option = str(input('Escolha uma opção: '))
    if (option == '1'):
        newplayer()
    if (option == '2'):
        seleciona()


print('Você saiu do jogo. E, lembre-se: "A habilidade de falar não o torna inteligente"')
