from database.connection import get_db_connection


def add_or_update_entry(user_id, date, mood, sleep, motivation, reflection):
    """
    Adds an entry for a particular user on a particular day if one doesn't already exist,
    or updates it if it does
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            if get_entry(user_id, date) is not None:
                cursor.execute("""
                         UPDATE tracker
                            SET mood = %s, sleep = %s, motivation = %s, reflection = %s
                          WHERE user_id = %s AND date = %s
                    """, [mood, sleep, motivation, reflection, user_id, date])
            else:
                cursor.execute("""
                    INSERT INTO tracker
                                (user_id, date, mood, sleep, motivation, reflection)
                         VALUES (%s, %s, %s, %s, %s, %s)
                    """, [user_id, date, mood, sleep, motivation, reflection])
            connection.commit()


def get_entry(user_id, date):
    """
    Gets the entry for a particular user on a particular day, if it exists
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""
                            SELECT mood, sleep, motivation, reflection
                              FROM tracker
                             WHERE user_id = %s
                               AND date = %s
                            """, [user_id, date])
            result = cursor.fetchone()
            return result


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
