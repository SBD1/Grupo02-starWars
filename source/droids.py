from db.database import connect, query, close


def take_droid(jogador_id, droid_id):
    [cursor, connection] = connect()
    insert_script = str(
        'INSERT INTO instancia_de_droid( jogador, nro_serie) VALUES (%s, %s);')
    insert_values = (jogador_id, droid_id)

    cursor.execute(insert_script, insert_values)

    connection.commit()

    close(connection, cursor)

def use_droid_hability(instancia_id):
    [cursor, connection] = connect()

    droid_id = query(cursor, f"SELECT nro_serie FROM instancia_de_droid WHERE id='{instancia_id}';")
    
    habilidade_id = query(cursor, f"SELECT habilidade FROM droid WHERE id='{droid_id}';")
    
    habilidade = query(cursor, f"SELECT * FROM habilidade WHERE id='{habilidade_id}';")
    
    close(connection, cursor)
    print(f'Droid usou {habilidade.nome} ({habilidade.descricao})')
