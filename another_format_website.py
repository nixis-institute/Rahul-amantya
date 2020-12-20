from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('fnl_lnk','r').read().split('\n')
fw = open('honda_links_data.csv','w',encoding='utf-8',newline="")
row = csv.writer(fw)
for i in fr[5000:]:
    try:
        r = s.get(i)
        tree = html.fromstring(r.content)
        soup = bs(r.content,'html.parser')
        if(soup.find('div','carDetails')):
            full_name = soup.find('div','carDetails').find('h3').text
        else:
            full_name = 'Not given'
        brand = ''.join(tree.xpath('//h1[@style="width: 620px;"]//text()')).strip()[0:6]
        #if(tree.xpath('//th[contains(string(),"Model:")]//following-sibling::td//text()')[0]):
        try:
            model = ''.join(tree.xpath('//th[contains(string(),"Model:")]//following-sibling::td//text()')[0]).strip()
        except:
            model ='Not given'
            pass
        mdoel1 = ''.join(tree.xpath('//div[@class="carDetails"]//h3[contains(string(),"TOYOTA PRIUS - Car Details")]//text()'))[6:]
        location = ''.join(tree.xpath('//th[contains(string(),"Location:")]//following-sibling::td//text()')).strip()
        year = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Registration Year:")]//following-sibling::td//text()')).strip()
        transmission = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Transmission:")]//following-sibling::td//text()')).strip()
        drive_chain = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Drive:")]//following-sibling::td//text()')).strip()
        body_type = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Body Type:")]//following-sibling::td//text()')).strip()
        mileage = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Mileage:")]//following-sibling::td//text()')).strip()
        # if(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Fuel:")]//following-sibling::td//text()')[0]):
        try:
            fuel = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Fuel:")]//following-sibling::td//text()')[0]).strip()
        except:
            fuel = 'Not given'
            pass
            
        streering = ''.join(tree.xpath('//div[@class="carDetails"]//th[contains(string(),"Steering:")]//following-sibling::td//text()')).strip()
        row.writerow([
            full_name,
            brand,
            model,
            mdoel1,
            streering,
            location,
            year,
            transmission,
            drive_chain,
            body_type,
            mileage,
            'Used',
            i
        ])
        print(i)
    except:
        print("Exception!")
        pass
