from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import re
import csv
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('dubicars_used_cars_links','r').read().split('\n')
fw = open('outputfile.csv','w',encoding='utf-8',newline="")
row = csv.writer(fw)
for links in fr[:5000]:
    r = s.get(links)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    brand = ''.join(tree.xpath('//section[@id="item-details"]//table//tr[contains(string(),"Make:")]//following-sibling::td//text()')).strip()
    # brand = ''.join(tree.xpath('//section[@id="item-details"]//table//tr//th[contains(string(),"Make:")]//following-sibling::td//text()')).string()
    model = ''.join(tree.xpath('//section[@id="item-details"]//table//tr//th[contains(string(),"Model:")]//following-sibling::td//text()')).strip()
    year = ''.join(tree.xpath('//section[@id="item-details"]//table//tr[contains(string(),"Year:")]//following-sibling::td//text()')).strip()
    car_type = ''.join(tree.xpath('//section[@id="item-details"]//table//tr[contains(string(),"Car type:")]//following-sibling::td//text()')).strip()
    mileage = ''.join(tree.xpath('//section[@id="item-details"]//table//tr[contains(string(),"Kilometers:")]//following-sibling::td//text()')).strip()
    transmission = ''.join(tree.xpath('//section[@id="item-details"]//table//tr[contains(string(),"Gearbox:")]//following-sibling::td//text()')).strip()
    fuel = ''.join(tree.xpath('//section[@id="item-details"]//table//tr[contains(string(),"Fuel:")]//following-sibling::td//text()')).strip()
    price = ''.join(tree.xpath('//strong[@class="money total-price"]//text()')).strip().replace('AED ','')
    location = ''.join(tree.xpath('//span[@property="name"]//text()')).strip()
    if(location):
        locat = tree.xpath('//span[@property="name"]//text()')[1]
    else:
        locat = 'Not given'
    
    row.writerow([
        links,
        brand,
        model,
        car_type,
        transmission,
        fuel,
        locat,
        year,
        price,
        mileage
    ])
    print(links)