from requests import Session
from lxml import html
from bs4 import BeautifulSoup as bs
import csv
lnk = []
s = Session()
s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"
url = 'https://www.amazon.in/s?i=electronics&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031&page={}'
f = open('output.csv','w',encoding='utf-8',newline='')
row = csv.writer(f)
for i in range(0,10):
    r = s.get(url.format(i))
    soup = bs(r.content,'html.parser')
    div = soup.find_all('div','a-section a-spacing-none')
    for div_t in div:
         n = div_t.find('a','a-link-normal s-navigation-item')
         if(n):
             lnk.append(n.get('href'))
    # len(lnk)
    print(url.format(i))
print(len(lnk))

# for deltails in lnk:
#     res = s.get(deltails)
#     tree1 = html.fromstring(res.text)
#     name = ''.join(tree1.xpath('//span[@class="a-size-large product-title-word-break"]//text()')).strip().replace('\n','').replace('\r','')
#     price = ''.join(tree1.xpath('//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]//text()')).strip()
#     row.writerow([
#         name, price,deltails
#     ])