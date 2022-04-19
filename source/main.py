from db.database import connect, query, close

[cursor, connection] = connect()

print(query(cursor, "select * from objetivo where roteiro = 'Episódio I - Parte I - Surgimento dos clones'"))

close(connection, cursor)
