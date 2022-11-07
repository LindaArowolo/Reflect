import unittest
from api.mock_activity_api import mock_activity_data


class TestMockActivityApi(unittest.TestCase):

    def test_activity(self):
        mock_activity_api = mock_activity_data
        self.assertIn("Go on a 3-5km walk, try listening to your favourite playlist whilst doing so.", mock_activity_api)
        self.assertNotIn("Try running a marathon", mock_activity_api)


if __name__ == '__main__':
    unittest.main()
