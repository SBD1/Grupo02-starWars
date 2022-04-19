from db.database import connect, query, close

player = str(input('Insira o nome do jogador: '))
[cursor, connection] = connect()
insert_script = str('INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);')
insert_values = (player, 'humano', 1000, 100,
                 10, 1, 'Padawan', 5, 5, 5, 5, 15)

cursor.execute(insert_script, insert_values)

connection.commit()
#print(query(cursor, insert_script))


close(connection, cursor)
