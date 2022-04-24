from db.database import connect, query, close

[cursor, connection] = connect()

latitude = 0
longitude = 0
idLocalizacao = query(cursor,
                      f"SELECT id FROM localizacao WHERE latitude={latitude} AND longitude={longitude};")
idLocalizacao = idLocalizacao[0]
idLocalizacao = idLocalizacao[0]
print(idLocalizacao)
npc = query(
    cursor, f"SELECT nome FROM npc WHERE localizacao={idLocalizacao};")
print(npc)
idNPC = query(
    cursor, f"SELECT id FROM npc WHERE nome=\'{npc}\';")

print(idNPC)

close(connection, cursor)
