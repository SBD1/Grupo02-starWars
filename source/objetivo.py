from pickle import TRUE
from db.database import connect, query, close


def consultaTodosObjetivo(roteiro):
    [cursor, connection] = connect()
    objetivos = query(
        cursor, f'select * from objetivo where roteiro = \'{roteiro}\';')
    close(connection, cursor)
    i = 0
    for row in objetivos:
        i = i+1
        if(row[5] == TRUE):
            classificacao = 'primário'
        else:
            classificacao = 'secundário'
        print(
            f'''{i} - {row[6]} | Ordem: {row[6]} | Classificação: {classificacao} | midichlorians: {row[3]} | Pontos da força: {row[4]}''')
    input(f'\n\nAperte qualquer tecla para sair: ')
