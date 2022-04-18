from db.database import connect, query, close


def menu(player, titulo, id_campoastronomico):
    option = '0'
    latitude = 0
    longitude = 0
    nome_campo = consultaCampo(id_campoastronomico)
    atmosfera_campo = consultaAtmosfera(id_campoastronomico)

    while (option != 'Q'):
        print('********************* Menu de ações *********************')
        print(f'''
          Você está em ({latitude},{longitude}) no campo astronômico {nome_campo}. A atmosfera é {atmosfera_campo}!

          [A] Ande para o mapa da esquerda
          [S] Ande para o mapa de baixo
          [D] Ande para o mapa da direita
          [W] Ande para o mapa de cima
          [M] Ver mapa
          [I] Inventário
          [C] Características
          [O] Ordem e Rank
          [L] Listar objetos que você pode interagir
          [Q] Sair do jogo
          ''')
        option = str(input('Escolha uma opção: '))
        if (option == 'A' or option == 'a'):
            print('Você andou para a esquerda!\n')
            latitude = latitude - 1
        if (option == 'S' or option == 's'):
            print('Você andou para baixo!\n')
            longitude = longitude + 1
        if (option == 'D' or option == 'd'):
            print('Você andou para a direita!\n')
            latitude = latitude + 1
        if (option == 'W' or option == 'w'):
            print('Você andou para cima!\n')
            longitude = longitude - 1
        if (option == 'M' or option == 'm'):
            print('Ver mapa --> Faz consulta no banco e mostra a imagem do mapa')
        if (option == 'I' or option == 'i'):
            print(
                'Acessa inventário --> Faz consulta no banco dos itens que o jogador possui')
        if (option == 'C' or option == 'c'):
            consultaCaracteristica(player)
        if (option == 'O' or option == 'o'):
            print(
                'Ordem e rank --> Faz uma consulta no banco e mostra o rank e a porcentagem da força')
        if (option == 'L') or option == 'l':
            print('Listar objetos que você pode interagir --> Faz consulta no banco com os NPCs, Opnentes ou itens que estão no mapa')


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
