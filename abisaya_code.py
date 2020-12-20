from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import re
import csv
from googletrans import Translator
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('abis','r').read().split('\n')
fw = open('abishaya_data.csv','w',encoding='utf-8',newline="")
row = csv.writer(fw)
trans = Translator()

# def translate_data(pr,brd,mod,yar,cit,trans):

for i in fr:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    price = ''.join(tree.xpath('//div[@class="vif_info"]//h3//text()')).strip().replace(' ريال سعودي','')
    # brand = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string()," تويوتا")]//text()')).strip()
    # model = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string(),"Model: ")]//text()')).strip()
    # year = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string(),"Year: ")]//text()')).strip()
    # mileage = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string(),"Mileage:")]//text()')).strip()
    # city = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string(),"City:")]//text()')).strip()
    # transmission = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string(),"Gearbox: ")]//text()')).strip() 
    # drive_type = ''.join(tree.xpath('//div[@class="vif_info"]//ul//li[contains(string(),"Drive Type: ")]//text()')).strip()
    all_data = '|'.join(tree.xpath("//div[@class='vif_info']//li//text()"))
    row.writerow([
        i,
        # brand,
        # model,
        # city,
        # transmission,
        # drive_type,
        # mileage,
        price,
        all_data,
        # 'Patrol',
        # 'cars_type',
        # 'Used cars'
    ])
    print(i)