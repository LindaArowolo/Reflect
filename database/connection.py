import mysql.connector
from config import HOST, DATABASE, USER, PASSWORD


def get_db_connection():
    connection = mysql.connector.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    return connection
