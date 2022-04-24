from db.database import connect, query, close


def npc_dialogo(npc_id, player):
    [cursor, connection] = connect()

    # CONSULTA nome, dialogo e item do NPC
    npc = query(
        cursor, f"SELECT nome,dialogo,item FROM npc WHERE id='{npc_id}';")
    npc = npc[0]

    # IMPRIME DIALOGO DO NPC
    print(f'''
          
    {npc[0]} diz:
    
          {npc[1]}
          
          ''')

    input(f'\n\nAperte qualquer tecla para sair: ')

    interage = query(
        cursor, f"SELECT * FROM interage WHERE jogador='{player[0]}' AND npc='{npc_id}';")
    if not interage:
        # CHAMA FUNÇÃO darItem
        darItem(npc[2], player)

        # INSERE UMA INSTANCIA DE ITEM NA TABELA instancia_item_jogador
        insert_script = str(
            'INSERT INTO interage(jogador, npc) VALUES (%s, %s);')
        insert_values = (player, npc_id)
        cursor.execute(insert_script, insert_values)
        connection.commit()
    else:
        print('\nVocê já recebeu este item!\n')

    close(connection, cursor)


def darItem(item, jogador):
    [cursor, connection] = connect()

    # INSERE UMA INSTANCIA DE ITEM NA TABELA instancia_item_jogador
    insert_script = str(
        'INSERT INTO instancia_item_jogador(item, jogador) VALUES (%s, %s);')
    insert_values = (item, jogador)
    cursor.execute(insert_script, insert_values)
    connection.commit()

    # CONSULTA O NOME DO ITEM QUE O NPC DEU PARA O JOGADOR
    nomeItem = query(cursor, f"SELECT nome FROM item WHERE id ={item}")
    nomeItem = nomeItem[0]
    print(f'\nVocê recebeu o item: {nomeItem[0]}!\n')

    # VERIFICA SE O ITEM É UTILIZAVEL, SE FOR UTILIZAVEL, ADICIONA NOVA HABILIDADE
    habilidadeDoItemUtilizavel = query(
        cursor, f"SELECT habilidade FROM item_utilizavel WHERE item ={item}")
    if not habilidadeDoItemUtilizavel:
        habilidadeDoItemUtilizavel = 0
    else:
        habilidadeDoItemUtilizavel = habilidadeDoItemUtilizavel[0]

        # INSERE A NOVA HABILIDADE NO BANCO
        insert_script = str(
            'INSERT INTO possui(jogador, habilidade) VALUES (%s, %s);')
        insert_values = (jogador, habilidadeDoItemUtilizavel[0])
        connection.commit()

        # CONSULTA NOME DA HABILIDADE
        nomeHabilidade = query(
            cursor, f"SELECT nome FROM habilidade WHERE id ={habilidadeDoItemUtilizavel[0]}")
        nomeHabilidade = nomeHabilidade[0]
        print(f'\nVocê recebeu a habilidade: {nomeHabilidade[0]}!\n')

    close(connection, cursor)
