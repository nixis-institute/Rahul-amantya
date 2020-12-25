from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('cat10','w',encoding='utf-8')
url = 'https://www.rack-a-tiers.com/product-category/wire-management/'
r = s.get(url)
soup = bs(r.content,'html.parser')
tree = html.fromstring(r.content)
div = soup.find_all('div','product-category')
p = soup.find_all('p','name product-title woocommerce-loop-product__title')

if(div):
    for i in div: 
        a = i.find('a') 
        # print(a.get('href'))
        fr.write(a.get('href')+'\n')
    print(url)
elif(p):
    for i in p: 
        a = i.find('a') 
        # print(a.get('href'))
        fr.write(a.get('href')+'\n')
    print(url)
