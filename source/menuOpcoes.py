def menu(player):
    option = '0'

    while (option != 'Q'):
        print('Menu de açõs')
        print('''
          [A] Ande para o mapa da esquerda
          [S] Ande para o mapa de baixo
          [D] Ande para o mapa da direita
          [W] Ande para o mapa de cima
          [M] Ver mapa
          [I] Inventário
          [C] Características
          [O] Ordem e Rank
          [L] Listar objetos que você pode interagir
          [Q] Sair do episódio
          ''')
        option = str(input('Escolha uma opção: '))
        if (option == 'A'):
            print('Muda mapa')
        if (option == 'S'):
            print('Muda mapa')
        if (option == 'D'):
            print('Muda mapa')
        if (option == 'W'):
            print('Muda mapa')
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
