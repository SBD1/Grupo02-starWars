# Load dotenv
import os
from dotenv import load_dotenv
load_dotenv()

import psycopg2

def connect():
  connection = psycopg2.connect( host     = os.getenv("DB_HOST"),
                                 dbname   = os.getenv("DB_NAME"), 
                                 user     = os.getenv("DB_USER"),
                                 password = os.getenv("DB_PASS"),
                                 port     = os.getenv("DB_PORT"))
  cursor = connection.cursor()
  print('Conectado')

  return cursor, connection

def query(cursor, query):
  try:
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows  
  except Exception as err:
      print(err, file=sys.stderr)
      return None

def close(connection, cursor):
  cursor.close()
  connection.close()
  print('Desconectado')
