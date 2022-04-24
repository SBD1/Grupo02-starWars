from db.database import connect, query, close
from enfrentar import enfrentar
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

    # id oponente
    idOponente = query(
        cursor, f"SELECT oponente, id FROM instancia_oponente WHERE localizacao={idLocalizacao};")
    if not idOponente:
        idOponente = 0
    else:
        idOponente = idOponente[0]
        idinstanciaOponente = idOponente[1]
        idOponente = idOponente[0]
        oponente = query(
            cursor, f"SELECT nome FROM oponente WHERE id={idOponente};")
        oponente = oponente[0]

    # Nave
    nroSerieNave = query(
        cursor, f"SELECT nro_serie FROM instancia_de_nave WHERE localizacao={idLocalizacao};")
    if not nroSerieNave:
        nroSerieNave = 0
    else:
        nroSerieNave = nroSerieNave[0]
        nroSerieNave = nroSerieNave[0]
        nave = query(
            cursor, f"SELECT nome FROM nave WHERE nro_serie=\'{nroSerieNave}\';")
        nave = nave[0]
    close(connection, cursor)

    # IMPRIME MENSAGEM DE INTERAÇÃO NA TELA
    if (idOponente != 0):
        print(f'[E] Enfrentar {oponente[0]}')
    if (instanciaitem != 0):
        print(f'[I] Pegar {item[0]}')
    if (npc != 0):
        print(f'[C] Conversar com {npc[0]}')
    if (nroSerieNave != 0):
        print(f'[P] Pilotar {nave[0]} ')
    print('[0] Sair')

    option = str(input('Escolha uma opção: '))

    if(option == 'E' or option == 'e'):
        print(f"Lutando com {oponente[0]}")
        enfrentar(idJogador, idinstanciaOponente, idOponente)

    if(option == 'i' or option == 'I'):
        print(f"Pegando {item[0]}")

    if(option == 'P' or option == 'p'):
        print(f"Pilotando {nave[0]}")

    if(option == 'C' or option == 'x'):
        npc_dialogo(idNPC[0], idJogador)

    input(f'\n\nAperte qualquer tecla para sair: ')
