from db.database import connect, query, close

[cursor, connection] = connect() 

print(query(cursor, "SELECT * FROM jogador;"))

close(connection, cursor)
