from db.database import connect, query, close

[cursor, connection] = connect()

latitude = 8
longitude = -9
idLocalizacao = query(cursor,
                      f"SELECT id FROM localizacao WHERE latitude={latitude} AND longitude={longitude};")
if not idLocalizacao:
    idLocalizacao = 0
else:
    idLocalizacao = idLocalizacao[0]
    idLocalizacao = idLocalizacao[0]

print(idLocalizacao)

close(connection, cursor)
