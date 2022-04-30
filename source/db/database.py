# Load dotenv
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def connect():
    connDatabase = psycopg2.connect(host=os.getenv("DB_HOST"),
                                  dbname=os.getenv("DB_NAME"),
                                  user=os.getenv("DB_USER"),
                                  password=os.getenv("DB_PASS"),
                                  port=os.getenv("DB_PORT"))
    cursorDatabase = connDatabase.cursor()

    return cursorDatabase, connDatabase


def query(cursor, query):
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as err:
        print(err)
        return None


def close(connection, cursor):
    cursor.close()
    connection.close()
    # print('Desconectado')
