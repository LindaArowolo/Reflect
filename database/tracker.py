from database.connection import get_db_connection


def add_entry(user_id, date, mood, sleep, motivation, reflection):
    """
    Adds a new user to the database.
    Raises an error if the email already exists in the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""
                INSERT INTO tracker
                            (user_id, date, mood, sleep, motivation, reflection)
                     VALUES (%s, %s, %s, %s, %s, %s)
                """, [user_id, date, mood, sleep, motivation, reflection])
            connection.commit()


def entry_exists(user_id, date):
    """
    Checks whether an entry already exists for a particular user on a particular day
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""
                            SELECT *
                              FROM tracker
                             WHERE user_id = %s
                               AND date = %s
                            """, [user_id, date])
            result = cursor.fetchone()
            return True if result is not None else False


def get_averages(user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""
                            SELECT ROUND(AVG(mood), 1) AS average_mood,
                                   ROUND(AVG(sleep), 1) AS average_sleep,
                                   ROUND(AVG(motivation), 1) AS average_motivation
                              FROM tracker
                             WHERE user_id = %s AND date >= subdate(curdate(), 30);
                            """, [user_id])
            result = cursor.fetchone()
            return result
