import smtplib
from email.message import EmailMessage
from requests import Session
from bs4 import BeautifulSoup as bs
import requests
from plyer import notification 
import re
#import psycopg2
import time
import mysql.connector as sqltor
s = Session()
s.headers["User-Agent"] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
proxy = {"https":"http://scraperapi:1a5defb411e6c1f0a49a007f0d0fd972@proxy-server.scraperapi.com:8001"}

def email_alert(subject,body,to): 
    msg = EmailMessage() 
    msg.set_content(body) 
    msg['subject'] = subject 
    msg['to']=to 
    
    user = "Dulist101@gmail.com" 
    msg ['from']=user
    password= "pumfkkcgfezawxfb" 
    server = smtplib.SMTP("smtp.gmail.com",587) 
    server.starttls() 
    server.login(user,password) 
    server.send_message(msg) 
    server.quit()
        
mycon = sqltor.connect(user="root",password="rahul",host="localhost",database="scrapper_db",auth_plugin="mysql_native_password")
mycur = mycon.cursor()
links = open("link1.txt").read().split('\n')

query = "delete from names"
mycur.execute(query)
mycon.commit()

urls = []
#Testing Links and Scrapping Top Names
for i in links:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    if(soup.find("span","cta")):
        name = soup.find("div","soldBy").text
        urls.append(i)
        query = f"insert into names(name) values('{name}')"
        mycur.execute(query)
        mycon.commit()
    print(r.status_code)
    print(r.url)
print(len(urls))
while True:
    # Getting Top Names From DataBase
    query = "select * from names"
    mycur.execute(query)
    data = mycur.fetchall()
    names = [data[k][0] for k in range(len(data))]
    n_id = [data[y][1] for y in range(len(data))]

    #Scrapping Fluctuations of Name
    temp_names = []
    for j in urls:
        r = s.get(j)
        soup = bs(r.content,'html.parser')
        name = soup.find("div","soldBy").text
        temp_names.append(name)
    
    print(names)
    print(n_id)
    print(temp_names)

    if(len(names)==len(temp_names)):
        for u in range(len(names)):
            if(names[u]!=temp_names[u]):
                sku = re.search("https://www.noon.com/(.*?)/(.*?)/p",urls[u]).group(2)
                alert = f"Before : {names[u]} <> After : {temp_names[u]} | SKU : {sku}"
                notification.notify(title="Name Update",message=alert)
                email_alert("Name Update",alert,"medhruv.1908@gmail.com")
                query = f"update names set name = '{temp_names[u]}' where name = '{names[u]}' and id = '{n_id[u]}'"
                mycur.execute(query)
                mycon.commit()
