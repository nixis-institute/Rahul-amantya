from requests import Session
from lxml import html
from bs4 import BeautifulSoup as bs
import csv
import time
import random
s = Session()
s.headers["User-Agent"] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
fr = open('nlnk','r').read().split('\n')
fw = open('all_data.csv','w',encoding='utf-8',newline='')
row = csv.writer(fw)
for i in fr:
    rn = random.randint(1,5)
    time.sleep(rn)
    r = s.get(i)

    tree = html.fromstring(r.text)
    soup = bs(r.content,'html.parser')
    if(soup.find('h1','mb-15')):
        full_name = soup.find('h1','mb-15').text
    else:
        full_name = 'Not given'
    brand_model = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Make / Model")]//following-sibling::td//text()')
    # model = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Make / Model")]//following-sibling::td//text()')
    year = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Year")]//following-sibling::td//text()')
    drive_chain = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Driving Type")]//following-sibling::td//text()')
    engine = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Engine")]//following-sibling::td//text()')
    fuel = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Fuel")]//following-sibling::td//text()')
    transmission = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Transmission")]//following-sibling::td//text()')
    seats = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Passenger Capacity")]//following-sibling::td//text()')
    doors = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Doors")]//following-sibling::td//text()')
    location = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Location")]//following-sibling::td//text()')
    candition = tree.xpath('//td[@class="col-md-4 col-lg-4 col-xs-6 col-sm-4 bg_td_ligh" and contains(string(),"Grade")]//following-sibling::td//text()')
    row.writerow([
        full_name,
        brand_model,
        year,
        drive_chain,
        engine,
        fuel,
        transmission,
        seats,
        doors,
        location,
        candition,
        i
    ])
    print('Link :- {}'.format(i))
    print('Random time :- {}'.format(rn))
