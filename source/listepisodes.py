from db.database import connect, query, close
from menuOpcoes import menu
from util import clear


def episodios(jog):
    [cursor, connection] = connect()
    episodios = query(cursor, "SELECT * from ROTEIRO;")
    close(connection, cursor)

    print('\nLista de episódios:\n')
    i = 0
    for titulo in episodios:
        i = i+1
        print(f'[{i}] - {titulo[0]}')

    saida = '1'
    while (saida != '0'):

        aux = int(input('\nSelecione o episódio ou digite 0 para sair: '))
        if(aux != 0):
            clear()
            try:
                titulo = episodios[aux-1]
                
                print(titulo[3])
                for i in range(0, 1):
                    print(" ")

                print(titulo[2])
                option = input(f'\nEntrando no jogo.... Olá, {jog}! Continuar? (y/n) ')

                print('')

                if(option == 'y' or option == 'Y'):
                    menu(jog, titulo[0], titulo[1])
                saida = '0'
            except Exception as err:
                print('Episódio ainda não existe!\n')
        if(aux == 0):
            saida = '0'
    return 0
