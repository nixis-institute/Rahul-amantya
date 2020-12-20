from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
import re
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fw = open('lnks_all.csv','w',encoding='utf-8',newline="")
fr = open('fnl_lnk','r').read().split('\n')
row = csv.writer(fw)
for i in fr:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    year = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Model Year")]//following-sibling::strong//text()'))
    location = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Location")]//following-sibling::strong//text()'))
    mileage = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Car Driven")]//following-sibling::strong//text()'))
    trans = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Transmission:")]//following-sibling::strong//text()'))
    fuel = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Fuel Type:")]//following-sibling::strong//text()'))
    doors = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Number of Doors")]//following-sibling::strong//text()'))
    cylinders = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Number of Cylinders")]//following-sibling::strong//text()'))
    body_type = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Body Style:")]//following-sibling::strong//text()'))
    price = ''.join(tree.xpath('//span[@class="price-count h3 green bold block"]//text()')).strip().replace('SAR     ','')
    name = ''.join(tree.xpath('//div[@class="usedcar-banner-desc col-lg-9"]//h1//text()'))
    if(name):
        brand = ''.join(tree.xpath('//div[@class="usedcar-banner-desc col-lg-9"]//h1//text()')).strip().split()[1]
        model =  ''.join(tree.xpath('//div[@class="usedcar-banner-desc col-lg-9"]//h1//text()')).strip().split()[2]
        model2  = ''.join(tree.xpath('//div[@class="usedcar-banner-desc col-lg-9"]//h1//text()')).strip().split()[3]
    else:
        brand = 'not found'
        model = 'not found'
        model2 = 'not found'
    row.writerow([
        i,brand,model,model2,year,location,mileage,trans,fuel,doors,cylinders,body_type,price,
    ])
    print(i)
