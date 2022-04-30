from db.database import connect, query, close
from listepisodes import episodios


def seleciona():
    [cursor, connection] = connect()

    rows = query(cursor, "SELECT * FROM jogador;")

    close(connection, cursor)

    print('\n***********  Jogadores  ***********')

    for row in rows:
        print('*   - ' + row[1], end="")

        contador = 7 + len(row[1])

        while (contador < 35):
            print(' ', end="")
            contador += 1
        print('*')
    print('***********************************\n')

    aux = 0
    while(aux != 1):
        player = str(input('\nSelecione o jogador: '))
        for row in rows:
            if(player == row[1]):
                aux = 1
                inicia(player)

        if(aux != 1):
            print('\nJogador inválido! =(\n')


def inicia(player):
    option = input(f'\nDeseja inicar o jogo com o {player}? (y/n) ')

    if(option == 'y' or option == 'Y'):
        episodios(player)
