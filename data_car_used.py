from requests import Session
from lxml import html
from bs4 import BeautifulSoup as bs
import re
import csv
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('all_lnk','r').read().split('\n')
fw = open('all_data.csv','w',encoding='utf-8')
row = csv.writer(fw)
for i in fr:
    r = s.get(i)
    # soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    price = tree.xpath('//dl[contains(string(),"Car Price")]//following-sibling::dd//text()')
    engine_ = tree.xpath('//div[@class="salesPoint"]//text()')
    transmission = tree.xpath('//section[@class="spec"]//th[contains(string(),"Transmission")]//following-sibling::td//text()')
    steering = tree.xpath('//section[@class="spec"]//th[contains(string(),"Steerings")]//following-sibling::td//text()')
    mileage = tree.xpath('//section[@class="spec"]//th[contains(string(),"Mileage")]//following-sibling::td//text()')
    fuel = tree.xpath('//section[@class="spec"]//th[contains(string(),"Fuel")]//following-sibling::td//text()')
    engine_code = tree.xpath('//section[@class="spec"]//th[contains(string(),"Engine code")]//following-sibling::td//text()')
    drive_chain = tree.xpath('//section[@class="spec"]//th[contains(string(),"Drivetrain")]//following-sibling::td//text()')
    seats = tree.xpath('//section[@class="spec"]//th[contains(string(),"Seats")]//following-sibling::td//text()')
    brand = tree.xpath('//section[@class="keyword"]//li[contains(string(),"MITSUBISHI FUSO")]//text()')
    row.writerow([
        price,
        engine_,
        transmission,
        steering,
        mileage,
        fuel,
        engine_code,
        drive_chain,
        seats,
        brand,
        i
    ])
    print(i)

# l = ['Coloured Bits','Copper Wire Stripper','Fasteners','Hole Cutters & Accessories','Innovative Tools','Mag Daddy & Connectors','Pop-Up Outlets','Testers, Controls & Cleanup','Tool Bags, Belts & Safety','Tools, Flashlights & Books','Wire & Conduit Bending','Wire Management']
