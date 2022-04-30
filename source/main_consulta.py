from db.database import connect, query, close

[cursor, connection] = connect()

text = query(
    cursor, f"SELECT id, item FROM instancia_item_localizacao WHERE localizacao=5;")

print(text)


# print(idLocalizacao)
# print(idinstancia)
close(connection, cursor)
