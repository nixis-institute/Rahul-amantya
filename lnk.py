from bs4 import BeautifulSoup as bs
from requests import Session
import csv
from lxml import html
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
f = open('fnl_lnk', 'r',encoding='utf-8').read().split('\n')
fw = open('toyoto_data.csv','w',encoding='utf-8')
erro_lnk = open('erro_links.txt','w',encoding='utf-8')
# l = ['4RUNNER(2)','ALLEX(58)','bB(351)','C-HR(210)','DUET(3)','ESQUIRE(168)','FJ CRUISER(46)','GAIA(1)','HARRIER(543)','IPSUM(74)','KLUGER(52)','LAND CRUISER(237)','MAJESTA(1)','NADIA(2)','OPA(1)','PASSO(692)','RACTIS(598)','SAI(133)','TANK(31)','URBAN CRUISER(1)','VANGUARD(130)','WILL CYPHA(11)','YARIS(43)']
# url = 'https://www.sbtjapan.com/used-cars/toyota/{}}#listbox'
# url = "https://www.sbtjapan.com/used-cars/nissan/note/?model_code=&steering=all&drive=0&year_f=&month_f=&year_t=&month_t=&price_f=&price_t=&cc_f=0&cc_t=0&mile_f=0&mile_t=0&trans=0&savel=0&saveu=0&fuel=0&color=0&bodyLength=0&loadClass=0&engineType=0&truck_size=&location=&port=0&search_box=1&sold=&p_years=&bid_code=&pdate_f=&pdate_t=&locationIds=0&stock_ids=&d_country=76&d_port=119&ship_type=0&FreightChk=yes&currency=2&insurance=1&sort=0&psize=100&custom_search=&p_num={}#listbox"
# url = 'https://www.sbtjapan.com/used-cars/toyota/86#listbox'
row = csv.writer(fw)
for i in f[5000:]:
    try:
        r = s.get(i)
        # soup = bs(r.content,'html,parser')
        tree = html.fromstring(r.content)
        full_name = ''.join(tree.xpath('//h1//text()')).strip()
        full2_name = ''.join(tree.xpath('//ul[@class="title"]//p//text()')).strip()
        tran = ''.join(tree.xpath("""//th[contains(string(),"Transmission:")]//following-sibling::td//text()""")[0]).strip().replace('\n','')
        year = ''.join(tree.xpath("""//th[contains(string(),"Year:")]//following-sibling::td//text()""")).strip().replace('\n','')
        location = ''.join(tree.xpath("""//th[contains(string(),"Location:")]//following-sibling::td//text()""")).strip().replace('\n','')
        drive = ''.join(tree.xpath("""//th[contains(string(),"Drive:")]//following-sibling::td//text()""")[0]).strip().replace('\n','')
        doors = ''.join(tree.xpath("""//th[contains(string(),"Door:")]//following-sibling::td//text()""")).strip().replace('\n','')
        steering = ''.join(tree.xpath("""//th[contains(string(),"Steering:")]//following-sibling::td//text()""")[0]).strip().replace('\n','')
        seats = ''.join(tree.xpath("""//th[contains(string(),"Seats:")]//following-sibling::td//text()""")).strip().replace('\n','')
        engine_type = ''.join(tree.xpath("""//th[contains(string(),"Engine Type:")]//following-sibling::td//text()""")[0]).strip().replace('\n','')
        drive_chain = ''.join(tree.xpath("""//th[contains(string(),"Body Type:")]//following-sibling::td//text()""")).strip().replace('\n','')
        fuel = ''.join(tree.xpath("""//th[contains(string(),"Fuel:")]//following-sibling::td//text()""")[0]).strip().replace('\n','')
        mileage = ''.join(tree.xpath("""//th[contains(string(),"Mileage:")]//following-sibling::td//text()""")).strip().replace('\n','')
        cars_weight = ''.join(tree.xpath("""//th[contains(string(),"Gross Vehicle Weight:")]//following-sibling::td//text()""")).strip().replace('\n','')
        max_cars_weight = ''.join(tree.xpath("""//th[contains(string(),"Max Loading Capacity:")]//following-sibling::td//text()""")).strip().replace('\n','')
        color = ''.join(tree.xpath("""//th[contains(string(),"Color:")]//following-sibling::td//text()""")).strip().replace('\n','')
        model_code = ''.join(tree.xpath("""//th[contains(string(),"Model Code:")]//following-sibling::td//text()""")[0]).strip().replace('\n','')
        row.writerow([
            full_name,
            full2_name,
            tran,
            year,
            location,
            drive,
            doors,
            steering,
            seats,
            engine_type,
            drive_chain,
            fuel,
            mileage,
            cars_weight,
            max_cars_weight,
            color,
            model_code,
            i
        ])
        print(i)
    except:
        print("exeption!!")
        erro_lnk.write(i+'\n')
        pass
