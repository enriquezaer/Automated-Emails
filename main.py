import yagmail
import pandas
from news import NewFee

#df = pandas.read_csv("testFile.csv")

df = pandas.read_excel('people.xlsx')
for index, row in df.iterrows():
    news_feed = NewFee(interest=row['interest'], from_date='2022-03-20', to_date='2022-03-22')

    email = yagmail.SMTP(user="enriquezaer@gmail.com", password="G@mbit@01")
    email.send(to="hicah73770@superyp.com", subject="Hi there",
               contents="Hola este es el body!\nAlex", attachments="design.txt")

print(df)