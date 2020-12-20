from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
import time
import re
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0' 
fr = open('data_set_all_links','r',encoding='utf-8').read().split('\n')
fw = open('data_set_ksa.csv','w',encoding='utf-8')
row = csv.writer(fw)
for i in fr[3636:]:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    price = ''.join(tree.xpath('//div[@class="content-price"]//span[@class="price"]//text()')).strip()
    name_model = tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-make"]//div//a')
    if(name_model):
        name = tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-make"]//div//a//text()')[0]
        model = tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-make"]//div//a//text()')[1] 
    else:
        name = 'not given'
        model = 'not given'
    year = ''.join(tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-year"]//div[@class="text"]//text()')).strip()
    location = ''.join(tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-city"]//div[@class="text"]//text()')).strip()
    condition = ''.join(tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-condition"]//div[@class="text"]//text()')).strip()
    type_car = ''.join(tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-type"]//div[@class="text"]//text()')).strip()
    transmission = ''.join(tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-transmission"]//div[@class="text"]//text()')).strip()
    mileage = ''.join(tree.xpath('//div[@class="wrap-overview col-xs-12"]//ul[@class="vehicle-detail-overview"]//li[@class="v-mileage"]//div[@class="text"]//text()')).strip()
    row.writerow([
        i,
        name,
        model,
        transmission,
        type_car,
        location,
        condition,
        "patrol",
        mileage,
        price,
        
    ])
    print(i)