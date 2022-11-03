from database.connection import get_db_connection


def add_image(user_id, url):
    """
    Adds a new image to the scrapbook
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""
                INSERT INTO scrapbook
                            (user_id, image_url)
                     VALUES (%s, %s)
                """, [user_id, url])
            connection.commit()


def get_images(user_id):
    """
    Gets all scrapbook images for a particular user
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""
                            SELECT image_url
                              FROM scrapbook
                             WHERE user_id = %s
                            """, [user_id])
            results = cursor.fetchall()
            return results
