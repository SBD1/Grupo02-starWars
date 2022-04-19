from db.database import connect, query, close


def npc_dialogo(npc_id):
    [cursor, connection] = connect()

    npc = query(cursor, f"SELECT * FROM npc WHERE id='{npc_id}';")

    close(connection, cursor)

    print(f'''
          
    {npc.nome} diz:
    
          {npc.dialogo}
          
          ''')
