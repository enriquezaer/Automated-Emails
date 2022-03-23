import yagmail
import pandas
from news import NewFee

#df = pandas.read_csv("testFile.csv")

df = pandas.read_excel('people.xlsx')
for index, row in df.iterrows():
    news_feed = NewFee(interest=row['interest'], from_date='2022-03-20', to_date='2022-03-23')

    email = yagmail.SMTP(user="enriquezaer@gmail.com", password="G@mbit@01")
    email.send(to="nuhudesa@thichanthit.com", subject=f"Hola tus noticias sobre {row['interest']} para hoy",
               contents=f"Hola {row['name']}!  mira lo que hay sobre  {row['interest']} el dia de hoy.\n {news_feed.get()}\nAlex")

