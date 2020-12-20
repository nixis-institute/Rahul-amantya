from requests import Session
from lxml import html
from bs4 import BeautifulSoup as bs
import csv
s = Session()
s.headers["User-Agent"] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
fr = open('sedan.txt','r',encoding='utf-8').read().split('\n')
fw = open('sedan_outfie.csv','w',encoding='utf-8',newline='')
row = csv.writer(fw)
for i in fr[:10]:
    r = s.get(i)
    # soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.text)
    location = ''.join(tree.xpath("//th[contains(string(),'Location')]//following-sibling::td//text()")).strip()
    model = ''.join(tree.xpath("//th[contains(string(),'Version/Class')]//following-sibling::td//text()")).strip()
    mileage = ''.join(tree.xpath("//th[contains(string(),'Mileage')]//following-sibling::td//text()")).strip()
    engine_size = ''.join(tree.xpath("//th[contains(string(),'Engine Size')]//following-sibling::td//text()")[0]).strip()
    drive = ''.join(tree.xpath("//th[contains(string(),'Drive')]//following-sibling::td//text()")[0]).strip()
    transmision = ''.join(tree.xpath("//th[contains(string(),'Transmiss.')]//following-sibling::td//text()")[0]).strip()
    registration_ = ''.join(tree.xpath("//th[contains(string(),'RegistrationYear/month')]//following-sibling::td//text()")[0]).strip()
    fuel = ''.join(tree.xpath("//th[contains(string(),'Fuel')]//following-sibling::td//text()")).strip()
    manufacture_ = ''.join(tree.xpath("//th[contains(string(),'ManufactureYear/month')]//following-sibling::td//text()")[0]).strip()
    seats = ''.join(tree.xpath("//th[contains(string(),'Seats')]//following-sibling::td//text()")).strip()
    doors = ''.join(tree.xpath("//th[contains(string(),'Doors')]//following-sibling::td//text()")).strip()
    full_name = ''.join(tree.xpath('//div[@class="car-info-area cf"]//h1//text()')).strip()
    brand = ''.join(tree.xpath('//ul[@id="bread"]//li[contains(string(),"BMW")]//text()')).strip()
    row.writerow([
        full_name,
        brand,
        model,
        mileage,
        engine_size,
        drive,
        transmision,
        registration_,
        manufacture_,
        seats,
        doors,
        fuel,
        location,
        i
    ])
    print(i)