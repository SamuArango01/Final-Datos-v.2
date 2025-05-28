import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='nodo_eafit_lms',
            user='root',
            password='2014Samu230511?'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def execute_query(query, params=None, fetch=False):
    connection = get_connection()
    if not connection:
        return None
    result = None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        if fetch:
            result = cursor.fetchall()
        else:
            connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        connection.close()
    return result