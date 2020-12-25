from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
import re
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fw = open('chargers_links','w',encoding='utf-8',newline="")
url = 'https://www.power-sonic.com/chargers/'
r = s.get(url)
soup = bs(r.content,'html.parser')
a = soup.find_all('a','batteryranges__titlelink')
for i in a:
    if(i.get('href')):
        fw.write('https://www.power-sonic.com'+i.get('href')+'\n')
        print(i.get('href'))