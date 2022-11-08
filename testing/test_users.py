import unittest
import unittest.mock
import database.users


def get_mock_db_cursor(fetchone_return_value=None, fetchall_return_value=None):
    return unittest.mock.Mock(
        __enter__=lambda _: unittest.mock.Mock(
            execute=lambda query, params: None,
            fetchone=lambda: fetchone_return_value,
            fetchall=lambda: fetchall_return_value,
        ),
        __exit__=lambda *args: None,
    )


def get_mock_db_connection(mock_db_cursor):
    return unittest.mock.Mock(
        __enter__=lambda _: unittest.mock.Mock(
            cursor=lambda **kwargs: mock_db_cursor,
        ),
        __exit__=lambda *args: None,
    )


class TestUsers(unittest.TestCase):

    def test_email_available_with_available_email(self):
        email = "noshinislam98@gmail.com"
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.email_available(email)
            self.assertTrue(result)

    def test_email_available_with_unavailable_email(self):
        email = "noshin@gmail.com"
        matching_user = {"id": 1}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=matching_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.email_available(email)
            self.assertFalse(result)

    def test_get_user_with_credentials_with_correct_password(self):
        email = "noshinislam98@gmail.com"
        password = "Password1234"
        matching_user = {'id': 2, 'hashed_password': b'$2b$12$L8iht8.lDqoz1zwV82DUsOs2y3uWAd69Jnot5GmZHN/stzX2kZyTO'}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=matching_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.get_user_with_credentials(email, password)
            self.assertEqual(result, matching_user)

    def test_get_user_with_credentials_with_incorrect_password(self):
        email = "ash@live.com"
        password = "Trains1234"
        matching_user = {'id': 3, 'hashed_password': b'$2b$12$vEFCES46KSkb0z5HAGkyJOdDg/64N65ewna73lN/EBBzNvnzO8buy'}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=matching_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.get_user_with_credentials(email, password)
            self.assertIsNone(result)

    def test_get_user_with_credentials_with_invalid_user(self):
        email = "linda.a@hotmail.com"
        password = "Hello4321"
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.get_user_with_credentials(email, password)
            self.assertIsNone(result)

    def test_get_user_by_id_with_valid_id(self):
        id = 1
        matching_user = {"id": id, "name": "Noshin", "email": "noshin@gmail.com", "region": "Birmingham"}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=matching_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.get_user_by_id(id)
            self.assertEqual(result, matching_user)

    def test_get_user_by_id_with_invalid_id(self):
        id = 4
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.users.get_user_by_id(id)
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
