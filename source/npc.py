from db.database import connect, query, close


def npc_dialogo(npc_id):
    [cursor, connection] = connect()

    npc = query(cursor, f"SELECT nome,dialogo FROM npc WHERE id='{npc_id}';")
    npc = npc[0]
    close(connection, cursor)

    print(f'''
          
    {npc[0]} diz:
    
          {npc[1]}
          
          ''')
