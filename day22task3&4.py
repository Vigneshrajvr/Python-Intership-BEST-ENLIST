import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news?p=2')

soup =  BeautifulSoup(res.text, 'lxml')

titleRows=soup.find_all('tr','athing')

votesRows=soup.find_all('span','score')

titles=[]
votes=[]

for i in titleRows:
    title=i.find('a','storylink').text
    titles.append(title)

for i in votesRows:
    vote=i.text.split()[0]
    votes.append(vote)

print("Website Scrapped and the Values are stores in python objects")

DBDataRows=list(map(list,zip(titles,votes)))
import cx_Oracle
try:
    con = cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("Connected to DataBase")

    #cur.execute("create table WeBScrapDB(title varchar(100),votes number(10))")
    print("Table Created")
    cur.executemany("insert into WeBScrapDB values(:1,:2)",DBDataRows)
    con.commit()

    print("Printing the titles having more than 500 votes ")

    cur.execute("select * from WeBScrapDB where votes>500")

    DBRows=cur.fetchall()

    for i in DBRows:
        print("Title : ",i[0])
        print("Votes : ",i[1])

    
    print("Values Inserted")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
con.close()
