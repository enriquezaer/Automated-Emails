import yagmail
import pandas

#df = pandas.read_csv("testFile.csv")

df = pandas.read_excel('people.xlsx')

# email = yagmail.SMTP(user="enriquezaer@gmail.com", password="G@mbit@01")
# email.send(to="hicah73770@superyp.com", subject="Hi there",
#            contents="Hola este es el body!\nAlex", attachments="design.txt")

print(df)