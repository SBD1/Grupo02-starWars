from db.database import connect, query, close
from menuOpcoes import menu


def episodios(jog):
    [cursor, connection] = connect()
    episodios = query(cursor, "SELECT * from ROTEIRO;")
    close(connection, cursor)

    print('Lista de episódios: ')
    i = 1
    for titulo in episodios:
        print(f'[{i}] - {titulo[0]}')

    saida = '1'
    while (saida != '0'):

        aux = int(input('Selecione o episódio ou digite 0 para sair: '))
        if(aux != 0):
            try:
                titulo = episodios[aux-1]
                print(titulo[3])
                for i in range(0, 5):
                    print(" ")

                print(titulo[2])
                option = input(f'entrando no jogo.... Olá {jog}! (y/n) ')

                if(option == 'y'):
                    menu(jog, titulo[0], titulo[1])
                saida = '0'
            except Exception as err:
                print(err)
        if(aux == 0):
            saida = '0'
    return 0
