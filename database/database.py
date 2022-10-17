import mysql.connector
from Reflect import config

connection = mysql.connector.connect(
    user = config.USER,
    password = config.PASSWORD,
    database = config.DATABASE,
    host     = config.HOST
)

cursor = connection.cursor()

cursor.execute(""" INSERT INTO
                        Users
                        (email, name, region, password)
                        VALUES
                        ('linda5@gmail.com', 'Linda', 'London', 'Magic')
""")
connection.commit()

cursor.execute("""SELECT * FROM Users""")
print(cursor.fetchall())

cursor.execute(""" INSERT INTO
                    Tracker
                    (user_id, date, mood, sleep, motivation, journal)
                    VALUES
                    (1, '2022-10-14', 3, 2, 5, 'today got some stuff done')   
                    """)
connection.commit()

cursor.execute("""SELECT * FROM Tracker""")
print(cursor.fetchall())
