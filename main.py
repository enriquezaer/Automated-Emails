# API key : 3484c094a9bf4aac9d2e730a428c2e44
# www.newsapi.org

import requests
from pprint import pprint


class NewFee:

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "3484c094a9bf4aac9d2e730a428c2e44"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_data = from_date
        self.to_date = to_date
        self.language = language

    def get(self):

        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_data}" \
              f"&to={self.to_date}&" \
              f"language={self.language}&" \
              f"sortBy=popularity&" \
              f"apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

news_feed = NewFee(interest='nasa', from_date='2022-03-03', to_date='2022-03-09', language='es')
#news_feed = NewFee()
print(news_feed.get())

