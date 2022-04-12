from db.database import connect, query, close

[cursor, connection] = connect()
titulos = query(cursor, "SELECT titulo from ROTEIRO;")
close(connection, cursor)

print('Lista de episódios: ')
i = 1
for titulo in titulos:
    print(f'[{i}] - {titulo[0]}')

    aux = 1
    while (aux != '0'):
        aux = str(input('Selecione o episódio ou digite 0 para sair: '))
        if(aux != '0'):
            print('entrar no episodio')
            aux = '0'
