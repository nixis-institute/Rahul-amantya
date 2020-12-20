from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('final_links','r').read().split('\n')
fw = open('new_output1017.csv','w',encoding='utf-8')
row = csv.writer(fw)
for i in fr[1017:]:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    drive_chain = ''.join(tree.xpath('//table[@class="veh_table"]//tr//th[contains(string(),"2WD / 4WD")]//following-sibling::td//text()')).strip()
    engine_type = ''.join(tree.xpath('//table[@class="veh_table"]//tr//th[contains(string(),"Engine no.")]//following-sibling::td//text()')).strip()
    fuel_type = ''.join(tree.xpath('//table[@class="veh_table"]//tr//th[contains(string(),"Fuel")]//following-sibling::td//text()')).strip()
    seats = ''.join(tree.xpath('//table[@class="veh_table"]//tr//th[contains(string(),"Seats")]//following-sibling::td//text()')).strip()
    tranmission = ''.join(tree.xpath('//table[@class="veh_table"]//tr//th[contains(string(),"Transmission")]//following-sibling::td//text()')).strip()
    streeting = ''.join(tree.xpath('//table[@class="veh_table"]//tr//th[contains(string(),"Steering")]//following-sibling::td//text()')).strip()
    price = ''.join(tree.xpath('//dl[@class="p-vehicle-ditail-price-us-sp"]//dd//text()')).strip()
    brand_name = ''.join(tree.xpath('//p[@class="veh-breadcrumb"]//strong/text()')).split()[0]
    brand_name2 = ''.join(tree.xpath('//h2[@class="title_box_veh_h2"]//text()')).split()[0]
    row.writerow([brand_name,brand_name2,price,fuel_type,drive_chain,tranmission,engine_type,seats,streeting,i])
    print(i)
