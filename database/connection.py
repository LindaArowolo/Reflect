import mysql.connector
from Reflect.config import HOST, DATABASE, USER, PASSWORD


def get_db_connection():
    engine = mysql.connector.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    return engine
