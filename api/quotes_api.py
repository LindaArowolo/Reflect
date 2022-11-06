import requests
import random


class QuoteGenerator:

    def __init__(self):
        self.quote_data = self.get_all_quote_data()

    def get_random_quote(self):
        return random.choice(self.quote_data)['quote']

    @staticmethod
    def get_all_quote_data():
        response = requests.get("https://motivational-quote-api.herokuapp.com/quotes")
        data = response.json()
        return data
