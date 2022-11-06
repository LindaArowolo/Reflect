import requests
import random

from config import PEXELS_API_KEY


class PhotoGenerator:

    def __init__(self):
        self.api_key = PEXELS_API_KEY

    def get_random_picture(self):
        query_options = ['landscapes', 'oceans', 'lakes', 'mountains', 'trees', 'nature', 'beach']
        query = random.choice(query_options)
        return self.get_random_picture_by_query(query)

    def get_random_picture_by_query(self, query):
        response = requests.get(f'https://api.pexels.com/v1/search?query={query}', headers={'Authorization': self.api_key})
        data = response.json()
        photos = data['photos']
        return random.choice(photos)
