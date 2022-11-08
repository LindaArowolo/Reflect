import unittest
import unittest.mock
from api.mock_activity_api import create_activity_api


class TestMockActivityApi(unittest.TestCase):

    def test_get_activity(self):
        activity = "Practice gratitude. Make a list of the things that you are grateful for."
        with unittest.mock.patch("random.choice", return_value=activity):
            mock_activity_api = create_activity_api()
            with mock_activity_api.test_client() as client:
                response = client.get('/')
                self.assertEqual(response.json, {"activity": activity})


if __name__ == '__main__':
    unittest.main()
