import unittest
from api.quotes_api import QuoteGenerator


class TestQuoteApi(unittest.TestCase):

    def test_quotes(self):
        quotes_api = QuoteGenerator
        self.assertTrue('You will face many defeats in life, but never let yourself be defeated', quotes_api)
        self.assertIsNot('Sleep all day long', quotes_api)


if __name__ == '__main__':
    unittest.main()
