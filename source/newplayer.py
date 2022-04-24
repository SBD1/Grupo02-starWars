from db.database import connect, query, close


def newplayer():
    player = str(input('Insira o nome do jogador: '))
    [cursor, connection] = connect()
    insert_script = str('INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);')
    insert_values = (player, 'humano', 0, 100,
                     1, 'Jedi', 'Padawan', 1, 1, 1, 1, 15)

    cursor.execute(insert_script, insert_values)

    connection.commit()
    #print(query(cursor, insert_script))

    close(connection, cursor)
