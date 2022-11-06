import unittest
import unittest.mock
import database.users
import api.mock_activity_api
import api.quotes_api


# class TestAPI(unittest.TestCase):
#
#     def test_activity(self):
#         mock_activity_api = MockActivityApi
#         self.assertIn("Go on a 3-5km walk, try listening to your favourite playlist whilst doing so.", mock_activity_api.activity)
#         self.assertTrue()

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


class TestUserManagement(unittest.TestCase):

    def test_add_user(self):
        pass

    def test_email_available(self):
        pass

    def test_get_user_with_credentials(self):
        pass

    def test_get_user_by_id(self):
        pass


if __name__ == '__main__':
    unittest.main()
