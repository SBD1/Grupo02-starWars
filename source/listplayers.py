from db.database import connect, query, close
from listepisodes import episodios


def seleciona():
    [cursor, connection] = connect()

    rows = query(cursor, "SELECT * FROM jogador;")

    close(connection, cursor)
    print('Lista de jogadores cadastrados: ')
    for row in rows:
        print(row[1])

    aux = 0
    while(aux != 1):
        player = str(input('Selecione o jogador: '))
        for row in rows:
            if(player == row[1]):
                aux = 1
                inicia(player)

        if(aux != 1):
            print('Jogador inválido!')


def inicia(player):
    option = input(f'Deseja inicar o jogo com o {player}? (y/n) ')

    if(option == 'y'):
        episodios(player)
