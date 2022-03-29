import yagmail
import pandas
import datetime
import time
from news import NewFee

#df = pandas.read_csv("testFile.csv")

df = pandas.read_excel('people.xlsx')
while True:
    if datetime.datetime.now().hour == 5 and datetime.datetime.now().minute == 59:
        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d)")
            news_feed = NewFee(interest=row['interest'],
                               from_date=yesterday,
                               to_date=today)

            email = yagmail.SMTP(user="enriquezaer@gmail.com", password="G@mbit@01")
            email.send(to="waxibip611@jooffy.com", subject=f"Hola tus noticias sobre {row['interest']} para hoy",
                       contents=f"Hola {row['name']}!  mira lo que hay sobre  {row['interest']} el dia de hoy.\n {news_feed.get()}\nAlex")
    time.sleep(60)