from db.database import connect, query, close

[cursor, connection] = connect()

string = str(f"DELETE from possui where id = 2;")

cursor.execute(string)
connection.commit()


# print(idLocalizacao)
# print(idinstancia)
close(connection, cursor)
