from bs4 import BeautifulSoup as bs
from requests import Session
import csv
from lxml import html
s = Session()
n = 1
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
f = open('price.csv','w',encoding='utf-8',newline="")
lnk = open('unique_lnk_tc_v','r').read().split('\n')
row = csv.writer(f)
for links in lnk[25000:]:
    try:
        r = s.get(links)
        tree = html.fromstring(r.text)
        soup = bs(r.content,'html.parser')
        if(soup.find('h1','used-detail-ttl')):
            full = soup.find('h1','used-detail-ttl').text.strip().replace('\xa0',' ')
        else:
            full = "Not given"
        if(soup.find('h1','used-detail-ttl')):
            year = soup.find('h1','used-detail-ttl').text.strip().replace('\xa0',' ').split()[0]
        else:
            year = 'Not given'
        if(soup.find('h1','used-detail-ttl')):
            brand = soup.find('h1','used-detail-ttl').text.strip().replace('\xa0',' ').split()[1]
        else:
            brand = 'Not given'
        if(soup.find('h1','used-detail-ttl')):
            model = soup.find('h1','used-detail-ttl').text.strip().replace('\xa0',' ').split()[2]
        else:
            model = 'Not given'
        if(soup.find('div','car-price-body')):
            price = soup.find('div','car-price-body').text.strip()
        else:
            price = 'Not given'
        registration = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'Registration Year')]//following-sibling::td//text()""")
        maleg = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'Mileage')]//following-sibling::td//text()""")
        transmission = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'Transmission')]//following-sibling::td//text()""")
        fuel = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'Fuel')]//following-sibling::td//text()""")
        body1 = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'BodyStyle1')]//following-sibling::td//text()""")
        # body2 = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'BodyStyle2')]//following-sibling::td//text()""")
        drive_chain = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'Drive Type')]//following-sibling::td//text()""")
        condition = tree.xpath("""//th[@class='car-info-table-ttl' and contains(string(),'Condition')]//following-sibling::td//text()""")
        print(full)
        row.writerow([
            full,
            year,
            brand,
            model,
            price,
            registration,
            maleg,
            transmission,
            fuel,
            body1,
            # body2,
            drive_chain,
            condition,
            links
        ])
        print(links)
        print(n)
        n+=1
    except:
        print("Exception!")
        pass
