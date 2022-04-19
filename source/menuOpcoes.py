from db.database import connect, query, close
from npc import npc_dialogo
from objetivo import consultaTodosObjetivo


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
          [R] Ordem e Rank
          [O] Objetivos
          [L] Listar objetos que você pode interagir
          [Q] Sair do jogo
          ''')
        option = str(input('Escolha uma opção: '))
        if (option == 'A' or option == 'a'):
            print('Você andou para a esquerda!\n')
            latitude = latitude - 1
        if (option == 'S' or option == 's'):
            print('Você andou para baixo!\n')
            longitude = longitude - 1
        if (option == 'D' or option == 'd'):
            print('Você andou para a direita!\n')
            latitude = latitude + 1
        if (option == 'W' or option == 'w'):
            print('Você andou para cima!\n')
            longitude = longitude + 1
        if (option == 'M' or option == 'm'):
            print('Ver mapa --> Faz consulta no banco e mostra a imagem do mapa')
        if (option == 'I' or option == 'i'):
            print(
                'Acessa inventário --> Faz consulta no banco dos itens que o jogador possui')
        if (option == 'C' or option == 'c'):
            consultaCaracteristica(player)
        if (option == 'R' or option == 'r'):
            consultaOrdem(player)
        if (option == 'L') or option == 'l':
            print('Listar objetos que você pode interagir --> Faz consulta no banco com os NPCs, Opnentes ou itens que estão no mapa')
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


def consultaLocalização(latitude, longitude):
    [cursor, connection] = connect()

    conteudo = query(
        cursor, f"SELECT instancia_item,instancia_oponente,instancia_de_nave, npc FROM localizacao WHERE latitude={latitude} AND longitude={longitude};")
    conteudo = conteudo[0]
    npc = query(
        cursor, f"SELECT nome FROM npc WHERE id={conteudo[3]};")
    npc = npc[0]
    instanciaitem = query(
        cursor, f"SELECT item FROM instancia_item WHERE id={conteudo[0]};")
    instanciaitem = instanciaitem[0]
    item = query(
        cursor, f"SELECT nome FROM item WHERE id={instanciaitem[0]};")
    item = item[0]
    instanciaoponente = query(
        cursor, f"SELECT oponente FROM instancia_oponente WHERE id={conteudo[1]};")
    instanciaoponente = instanciaoponente[0]
    oponente = query(
        cursor, f"SELECT nome FROM oponente WHERE id={instanciaoponente[0]};")
    oponente = oponente[0]
    instancianave = query(
        cursor, f"SELECT nro_serie FROM instancia_de_nave WHERE id=\'{conteudo[2]}\';")
    instancianave = instancianave[0]
    nave = query(
        cursor, f"SELECT nome FROM nave WHERE nro_serie=\'{instancianave[0]}\';")
    nave = nave[0]
    print(f'''
          [E] Enfrentar {oponente[0]}
          [I] Pegar {item[0]}
          [C] Conversar com {npc[0]}
          [P] Pilotar {nave[0]} 
          ''')

    option = str(input('Escolha uma opção: '))

    if(option == 'E' or option == 'e'):
        print(f"Lutando com {oponente[0]}")

    if(option == 'i' or option == 'I'):
        print(f"Pegando {item[0]}")

    if(option == 'P' or option == 'p'):
        print(f"Pilotando {nave[0]}")

    if(option == 'C' or option == 'x'):
        npc_dialogo(conteudo[3])

    input(f'\n\nAperte qualquer tecla para sair: ')

    return
