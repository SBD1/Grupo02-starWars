from db.database import connect, query, close
from interacao import consultaLocalização
from objetivo import consultaTodosObjetivo


def menu(player, titulo, id_campoastronomico):
    option = 'q'
    latitude = 7
    longitude = -8
    nome_campo = consultaCampo(id_campoastronomico)
    atmosfera_campo = consultaAtmosfera(id_campoastronomico)

    while (option != '0'):
        print('********************* Menu de ações *********************')
        print(f'''
          Você está em ({longitude},{latitude}) no campo astronômico {nome_campo}. A atmosfera é {atmosfera_campo}!

          [A] Ande para o mapa da esquerda
          [S] Ande para o mapa de baixo
          [D] Ande para o mapa da direita
          [W] Ande para o mapa de cima
          [M] Ver mapa
          [I] Inventário
          [C] Características
          [R] Ordem e Rank
          [O] Objetivos
          [L] Listar objetos que você pode interagir
          [0] Sair do jogo
          ''')
        option = str(input('Escolha uma opção: '))
        if (option == 'A' or option == 'a'):
            longitude = longitude - 1
            idLocalizacao = consultaIDlocalizacao(latitude, longitude)
            if(idLocalizacao == 0):
                print('Você atingiu a fronteira do mapa')
                longitude = longitude + 1
            else:
                print('Você andou para a esquerda!\n')

        if (option == 'S' or option == 's'):
            latitude = latitude - 1
            idLocalizacao = consultaIDlocalizacao(latitude, longitude)
            if(idLocalizacao == 0):
                print('Você atingiu a fronteira do mapa')
                latitude = latitude + 1
            else:
                print('Você andou para baixo!\n')

        if (option == 'D' or option == 'd'):
            longitude = longitude + 1
            idLocalizacao = consultaIDlocalizacao(latitude, longitude)
            if(idLocalizacao == 0):
                print('Você atingiu a fronteira do mapa')
                longitude = longitude - 1
            else:
                print('Você andou para a direita!\n')

        if (option == 'W' or option == 'w'):
            latitude = latitude + 1
            idLocalizacao = consultaIDlocalizacao(latitude, longitude)
            if(idLocalizacao == 0):
                print('Você atingiu a fronteira do mapa')
                latitude = latitude - 1
            else:
                print('Você andou para cima!\n')

        if (option == 'M' or option == 'm'):
            consultaRegiao(id_campoastronomico)
        if (option == 'I' or option == 'i'):
            print(
                'Acessa inventário --> Faz consulta no banco dos itens que o jogador possui')
        if (option == 'C' or option == 'c'):
            consultaCaracteristica(player)
        if (option == 'R' or option == 'r'):
            consultaOrdem(player)
        if (option == 'L') or option == 'l':
            consultaLocalização(latitude, longitude)
        if (option == 'O' or option == 'o'):
            consultaTodosObjetivo(titulo)


def consultaCampo(id):

    [cursor, connection] = connect()

    nome = query(
        cursor, f'SELECT nome FROM campo_astronomico where id = {id};')

    nome = nome[0]
    close(connection, cursor)
    return nome[0]


def consultaAtmosfera(id):

    [cursor, connection] = connect()

    atmosfera = query(
        cursor, f'SELECT atmosfera FROM campo_astronomico where id = {id};')

    atmosfera = atmosfera[0]

    close(connection, cursor)
    return atmosfera[0]


def consultaCaracteristica(jogador):
    [cursor, connection] = connect()

    caracteristicas = query(
        cursor, f'select inteligencia, forca_fisica, agilidade, resistencia, raca, vida from jogador where nome = \'{jogador}\';')

    caracteristicas = caracteristicas[0]
    close(connection, cursor)
    print(f'''
        {jogador} é da raça {caracteristicas[4]}.
        Vida: {caracteristicas[5]}
        Inteligência: {caracteristicas[0]}
        Força Física: {caracteristicas[1]}
        Agilidade: {caracteristicas[2]}
        Resistência: {caracteristicas[3]}
    ''')
    input(f'\n\nAperte qualquer tecla para sair: ')

    return 0


def consultaOrdem(jogador):
    [cursor, connection] = connect()

    caracteristicas = query(
        cursor, f'select ordem, rank, midichlorians, espectro_forca, nivel from jogador where nome = \'{jogador}\';')
    caracteristicas = caracteristicas[0]
    close(connection, cursor)
    print(f'''
        {jogador} é da ordem {caracteristicas[0]} e tem rank {caracteristicas[1]}.
        Nível: {caracteristicas[4]}
        Midichlorians(xp): {caracteristicas[2]}
        Espectro da força: {caracteristicas[3]}
    ''')
    input(f'\n\nAperte qualquer tecla para sair: ')


def consultaIDlocalizacao(latitude, longitude):
    [cursor, connection] = connect()
    idLocalizacao = query(cursor,
                          f"SELECT id FROM localizacao WHERE latitude={latitude} AND longitude={longitude};")
    if not idLocalizacao:
        idLocalizacao = 0
    else:
        idLocalizacao = idLocalizacao[0]
        idLocalizacao = idLocalizacao[0]
    close(connection, cursor)
    return idLocalizacao

def consultaRegiao(id_campoastronomico):
    [cursor, connection] = connect()

    regiao = query(
        cursor, f'select nome, clima, governante, dominio, nivel from regiao where campo_astronomico = {id_campoastronomico};')

    regiao = regiao[0]
    close(connection, cursor)
    print(f'''
        Você está está em {regiao[0]} governada por {regiao[3]}.
    
        Clima: {regiao[1]}
        Nível da região: {regiao[4]}
        Dominio: {regiao[3]}
    ''')
    input(f'\n\nAperte qualquer tecla para sair: ')

    return 0