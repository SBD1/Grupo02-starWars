from db.database import connect, query, close


def pegar_item(idJogador, item):
    [cursor, connection] = connect()

    (idInstancia, idItem) = item

    try:
        insert_script = str(
            f'INSERT INTO instancia_item_jogador(item, jogador) VALUES (%s, %s);')
        insert_values = (idItem, idJogador)
        cursor.execute(insert_script, insert_values)
        connection.commit()

        delete_script = str(
            f"DELETE FROM instancia_item_localizacao WHERE id = {idInstancia};")
        cursor.execute(delete_script)
        connection.commit()

        close(connection, cursor)
    except:
        print('Inventário Cheio (10/10)')
