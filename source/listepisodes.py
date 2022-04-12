from db.database import connect, query, close


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
                print(titulo[2])
                for i in range(0, 5):
                    print(" ")

                print(titulo[1])
                print(f'entrando no jogo.... Olá {jog}!')
                saida = '0'
            except Exception as err:
                print(err)
        if(aux == 0):
            saida = '0'
    return 0
