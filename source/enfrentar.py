import random
from db.database import connect, query, close


def enfrentar(idjogador, idOponenteInstancia, idOponente, idLocalizacao):
    idjogador = idjogador[0]
    [cursor, connection] = connect()
    # INSERE NA TABELA COMBATE JOGADOR E INSTANCIA
    insert_script = str(
        'INSERT INTO combate(jogador, oponente) VALUES (%s, %s);')
    insert_values = (idjogador, idOponente)
    cursor.execute(insert_script, insert_values)
    connection.commit()

    # CONSULTA DADOS DO OPONENTE
    oponente = query(cursor, f"SELECT * FROM oponente WHERE id={idOponente}")
    oponente = oponente[0]

    # CONSULTA DADOS DO JOGADOR
    jogador = query(cursor, f"SELECT * FROM jogador WHERE id={idjogador}")
    jogador = jogador[0]

    # FAZ UMA LISTA COM OS IDs DE HABILIDADE QUE O JOGADOR POSSUI
    idHabilidades = query(
        cursor, f"SELECT habilidade FROM possui WHERE jogador={idjogador}")
    listHabilidade = []
    for idHabilidade in idHabilidades:
        idHabilidade = idHabilidade[0]
        listHabilidade.append(idHabilidade)

    # FAZ UMA LISTA COM OS nomes DAS HABILIDADES QUE O JOGADOR POSSUI
    listNomeHabilidade = []
    for idHabilidade in listHabilidade:
        nomeHabilidade = query(
            cursor, f"SELECT nome FROM habilidade WHERE id={idHabilidade}")
        nomeHabilidade = nomeHabilidade[0]
        nomeHabilidade = nomeHabilidade[0]
        listNomeHabilidade.append(nomeHabilidade)

    close(connection, cursor)

    nomeOponente = oponente[1]
    racaOponente = oponente[2]
    vidaOponente = oponente[3]
    midichloriansOponente = oponente[4]
    probabilidadeOponente = oponente[5]
    intOponente = oponente[6]
    forFisicaOponente = oponente[7]
    agiOponente = oponente[8]
    resisOponente = oponente[9]
    espectroForcaOponente = oponente[10]
    ataqueOponente = oponente[11]
    impactoOponente = oponente[12]
    caracteristicaOponente = oponente[13]

    nomeJogador = jogador[1]
    racaJogador = jogador[2]
    midichloriansJogador = jogador[3]
    vidaJogador = jogador[4]
    intJogador = jogador[8]
    forFisicaJogador = jogador[9]
    agiJogador = jogador[10]
    resisJogador = jogador[11]
    espectroForcaJogador = jogador[12]
    rodada = 0

    while (vidaOponente > 0 and vidaJogador > 0):
        rodada = rodada + 1
        # Mensagem de come??o de turno
        print(
            f'''************************************ RODADA {rodada} ***********************************


            ?? a sua vez, {nomeJogador}! Selecione uma habilidade para causar dano em {nomeOponente}:\n''')

        # lista as habilidades que o jogador pode usar
        i = 0
        for nome in listNomeHabilidade:
            i = i+1
            print(f'{i} - {nome}')

        # Usu??rio escolhe uma op????o de habilidade
        option = int(input('Escolha uma op????o: '))

        # Condi????o para n??o escolher fora da lista
        if(option <= len(listHabilidade)):
            id = listHabilidade[option-1]
            nome = listNomeHabilidade[option-1]
            [cursor, connection] = connect()
            habilidade = query(
                cursor, f"SELECT impacto, caracteristica FROM habilidade WHERE id={id}")
            close(connection, cursor)

            habilidade = habilidade[0]
            impacto = habilidade[0]
            caracteristica = habilidade[1]
            dano = 0
            if(caracteristica == 'Inteligencia'):
                dano = impacto * intJogador
            if(caracteristica == 'Forca Fisica'):
                dano = impacto * forFisicaJogador
            if(caracteristica == 'Agilidade'):
                dano = impacto * agiJogador

            # Aplica dano no oponente
            vidaOponente = vidaOponente - (dano - resisOponente)
            print(
                f'\nVoc?? usou {nome}! A vida do seu oponente ap??s o seu ataque ??: {vidaOponente}.\n')

            # Vez do oponente atacar
            print(f'Agora ?? a vez de {nomeOponente} jogar: \n\n')
            dano = 0
            if(caracteristicaOponente == 'Inteligencia'):
                dano = impactoOponente * intOponente
            if(caracteristicaOponente == 'Forca Fisica'):
                dano = impactoOponente * forFisicaOponente
            if(caracteristicaOponente == 'Agilidade'):
                dano = impactoOponente * agiOponente

            # Aplica dano no jogador
            if(dano < resisJogador):
                vidaJogador = vidaJogador
            else:
                vidaJogador = vidaJogador - (dano - resisJogador)
            print(
                f'{nomeOponente} usou {ataqueOponente}! A sua vida ap??s o seu ataque ??: {vidaJogador}.\n')

    # Em caso de vit??ria
    if(vidaJogador > vidaOponente):
        print(f'''\nVoc?? ganhou esta batalha!\n 
            Por sua vit??ria voc?? recebeu {midichloriansOponente} midichlorians!\n
            Voc?? recebeu {espectroForcaOponente} de Espectro da For??a gra??as a sua vit??ria!\n
        ''')
        midichloriansJogador = midichloriansJogador + midichloriansOponente
        espectroForcaJogador = espectroForcaJogador + espectroForcaOponente
        vidaJogador = 100
        probabilidade = random.randint(1, 100)

        # Probabilidade de ganhar itens
        print(
            f'Sua chance de ganhar exp??lio foi de {probabilidade} em {int(100 - probabilidadeOponente*100)}')
        if(probabilidade > (100 - probabilidadeOponente*100)):
            [cursor, connection] = connect()

            # CONSULTA O id DO ITEM
            idItem = query(
                cursor, f"SELECT item FROM instancia_oponente WHERE oponente={idOponente}")
            idItem = idItem[0]
            idItem = idItem[0]

            # INSERE O ITEM DENTRO DA TABELA DE ITENS DO JOGADOR
            insert_script = str(
                'INSERT INTO instancia_item_jogador(item, jogador) VALUES (%s, %s);')
            insert_values = (idItem, idjogador)
            cursor.execute(insert_script, insert_values)
            connection.commit()

            print(idOponente)
            print(idItem)
            nomeItem = query(
                cursor, f"SELECT nome FROM item WHERE id ={idItem}")
            nomeItem = nomeItem[0]
            print(f'\nVoc?? recebeu o item: {nomeItem[0]}!\n')

            # VERIFICA SE O ITEM ?? UTILIZAVEL, SE FOR UTILIZAVEL, ADICIONA NOVA HABILIDADE
            habilidadeDoItemUtilizavel = query(
                cursor, f"SELECT habilidade FROM item_utilizavel WHERE item ={idItem}")

            if not habilidadeDoItemUtilizavel:
                habilidadeDoItemUtilizavel = 0
            else:
                habilidadeDoItemUtilizavel = habilidadeDoItemUtilizavel[0]

            # INSERE A NOVA HABILIDADE NO BANCO
                insert_script = str(
                    'INSERT INTO possui(jogador, habilidade) VALUES (%s, %s);')
                insert_values = (idjogador, habilidadeDoItemUtilizavel[0])
                cursor.execute(insert_script, insert_values)
                connection.commit()

            # CONSULTA NOME DA HABILIDADE
                nomeHabilidade = query(
                    cursor, f"SELECT nome FROM habilidade WHERE id ={habilidadeDoItemUtilizavel[0]}")
                nomeHabilidade = nomeHabilidade[0]
                print(f'\nVoc?? recebeu a habilidade: {nomeHabilidade[0]}!\n')
            close(connection, cursor)
        # Ap??s if
        [cursor, connection] = connect()
        # REMOVE A INSTANCIA DO OPONENTE de instancia oponente
        if(idLocalizacao != 353):
            string = str(
                f"DELETE from instancia_oponente where id = {idOponenteInstancia};")

            cursor.execute(string)
            connection.commit()

        # ATUALIZA A EXPERI??NCIA GANHA AP??S COMBATE
        string = str(
            f"UPDATE jogador SET midichlorians = {midichloriansJogador} where id = {idjogador};")

        cursor.execute(string)
        connection.commit()

        close(connection, cursor)

    # Em caso de derrota
    else:
        print('\nVoc?? perdeu esta batalha! Treine mais um pouco para conseguir sair vitorioso na pr??xima aventura!')
        vidaJogador = 100
