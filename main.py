# API key : 3484c094a9bf4aac9d2e730a428c2e44
# www.newsapi.org

import requests
from pprint import pprint



class NewFee:

    def __int__(self, data):
        self.data = data

    def get(self):
        pass


response = requests.get("https://newsapi.org/v2/everything?q=bitcoins&from=2022-02-01&to=2022-02-01&sortBy=popularity&apiKey=3484c094a9bf4aac9d2e730a428c2e44")
content = response.text
pprint(content)


