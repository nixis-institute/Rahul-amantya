from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import re
import csv
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('fnal_links_uae','r').read().split('\n')
fw = open('d_outputfile.csv','w',encoding='utf-8',newline="")
row = csv.writer(fw)
for link in fr[15000:20000]:
    r = s.get(link)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    year = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Model Year")]//following-sibling::strong//text()')).strip()
    location = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Location")]//following-sibling::strong//text()')).strip()
    mileage = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Car Driven")]//following-sibling::strong//text()')).strip()
    transmission = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Transmission:")]//following-sibling::strong//text()')).strip()
    fuel = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Fuel Type:")]//following-sibling::strong//text()')).strip()
    body_type = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Body Style:")]//following-sibling::strong//text()')).strip()
    drive_chian = ''.join(tree.xpath('//ul[@class="features-list features-list-hrzntl used-car-features"]//li//div[@class="pull-left text-left"]//i[contains(string(),"Drive Type:")]//following-sibling::strong//text()')).strip()
    price = ''.join(tree.xpath('//div[@class="col-md-3 used-car-user-info"]//span[@class="price-count h3 green bold block"]//text()')).strip().replace('AED     ','')
    full_details = soup.find('h1')
    if(full_details):
        ful = soup.find('h1').text.strip()
    else:
        ful = 'Not given'
    if(full_details):
        condition = soup.find('h1').text.strip().split()[0]
    else:
        condition = 'Not given'
    if(full_details):
        brand = soup.find('h1').text.strip().split()[1]
    else:
        brand = 'Not given'
    if(full_details):
        model1 = soup.find('h1').text.strip().split()[2]
    else:
        model1 = 'Not given'
    if(full_details):
        model2 = soup.find('h1').text.strip().split()[3]
    else:
        model2 = 'Not given'
    row.writerow([
        link,
        ful,
        brand,
        model1,
        model2,
        condition,
        transmission,
        body_type,
        drive_chian,
        fuel,
        location,
        year,
        mileage,
        price
    ])
    print(link)