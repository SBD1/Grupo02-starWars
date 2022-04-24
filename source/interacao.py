from db.database import connect, query, close
from npc import npc_dialogo


def consultaLocalização(idJogador, latitude, longitude):
    [cursor, connection] = connect()
    idLocalizacao = query(cursor,
                          f"SELECT id FROM localizacao WHERE latitude={latitude} AND longitude={longitude};")
    idLocalizacao = idLocalizacao[0]
    idLocalizacao = idLocalizacao[0]

    # NPC
    npc = query(
        cursor, f"SELECT nome FROM npc WHERE localizacao={idLocalizacao};")
    if not npc:
        npc = 0
    else:
        npc = npc[0]
        idNPC = query(cursor, f"SELECT id FROM npc WHERE nome=\'{npc[0]}\';")
        idNPC = idNPC[0]

    # Instancia de item
    instanciaitem = query(
        cursor, f"SELECT item FROM instancia_item_localização WHERE localizacao={idLocalizacao};")
    if not instanciaitem:
        instanciaitem = 0
    else:
        instanciaitem = instanciaitem[0]
        item = query(
            cursor, f"SELECT nome FROM item WHERE id={instanciaitem[0]};")
        item = item[0]

    # Instancia oponente
    instanciaoponente = query(
        cursor, f"SELECT oponente FROM instancia_oponente WHERE localizacao={idLocalizacao};")
    if not instanciaoponente:
        instanciaoponente = 0
    else:
        instanciaoponente = instanciaoponente[0]
        oponente = query(
            cursor, f"SELECT nome FROM oponente WHERE id={instanciaoponente[0]};")
        oponente = oponente[0]

    # Nave
    instancianave = query(
        cursor, f"SELECT nro_serie FROM instancia_de_nave WHERE localizacao={idLocalizacao};")
    if not instancianave:
        instancianave = 0
    else:
        instancianave = instancianave[0]
        nave = query(
            cursor, f"SELECT nome FROM nave WHERE nro_serie=\'{instancianave[0]}\';")
        nave = nave[0]
    close(connection, cursor)

    # IMPRIME MENSAGEM DE INTERAÇÃO NA TELA
    if (instanciaoponente != 0):
        print(f'[E] Enfrentar {oponente[0]}')
    if (instanciaitem != 0):
        print(f'[I] Pegar {item[0]}')
    if (npc != 0):
        print(f'[C] Conversar com {npc[0]}')
    if (instancianave != 0):
        print(f'[P] Pilotar {nave[0]} ')
    print('[0] Sair')

    option = str(input('Escolha uma opção: '))

    if(option == 'E' or option == 'e'):
        print(f"Lutando com {oponente[0]}")

    if(option == 'i' or option == 'I'):
        print(f"Pegando {item[0]}")

    if(option == 'P' or option == 'p'):
        print(f"Pilotando {nave[0]}")

    if(option == 'C' or option == 'x'):
        npc_dialogo(idNPC[0], idJogador)

    input(f'\n\nAperte qualquer tecla para sair: ')
