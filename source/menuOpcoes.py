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
        if (option == 'A'):
            print('Você andou para a esquerda!\n')
            latitude = latitude - 1
        if (option == 'S'):
            print('Você andou para baixo!\n')
            longitude = longitude + 1
        if (option == 'D'):
            print('Você andou para a direita!\n')
            latitude = latitude + 1
        if (option == 'W'):
            print('Você andou para cima!\n')
            longitude = longitude - 1
        if (option == 'M'):
            print('Ver mapa --> Faz consulta no banco e mostra a imagem do mapa')
        if (option == 'I'):
            print(
                'Acessa inventário --> Faz consulta no banco dos itens que o jogador possui')
        if (option == 'C'):
            print('''Mostra as características --> Faz consulta no banco das características do personagem: 
            Inteligencia, força e etc. Deve-se ter opção para ele aumentar essas características a cada nível que ele passa''')
        if (option == 'O'):
            print(
                'Ordem e rank --> Faz uma consulta no banco e mostra o rank e a porcentagem da força')
        if (option == 'L'):
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
