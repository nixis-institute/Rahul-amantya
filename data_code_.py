from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
fr = open('lnks_file','r',encoding='utf-8').read().split('\n')
fw = open('outfile_.csv','w',encoding='utf-8',newline="")
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
row = csv.writer(fw)
for i in fr[1000:]:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    full_name = ''.join(tree.xpath('//div[@class="title-holder"]//h1//text()'))
    ful_data = soup.find('h1','title')
    # model = soup.find('h1','title').text.split()[1]
    # model1 = soup.find('h1','title').text.split()[2]
    if(ful_data):
        brand = soup.find('h1','title').text.split()[0]
        # model = soup.find('h1','title').text.split()[1]
        # model1 = soup.find('h1','title').text.split()[2]
    else:
        brand = 'Not given'
        # model = 'Not given'
        # model1 = 'Not given'
    try:
        if(ful_data):
            model = soup.find('h1','title').text.split()[1]
        else:
            model = 'Not given'
    except:
        print('Exception')
        model = 'Not given'
        pass

    try:    
        if(ful_data):
            model1 = soup.find('h1','title').text.split()[2]
        else:
            model1 = 'Not given'
    except:
        print('Exception')
        model1 = 'Not given'
        pass

    price = ''.join(tree.xpath('//div[@id="car-price"]//text()')).replace('AED ','').strip()
    location = ''.join(tree.xpath('//div[@class="col text-right text-black"]//text()')).strip()
    body_type = ''.join(tree.xpath('//div[@class="panel-body"]//div[@data-label="Body Type"]//text()')).strip()
    seats = ''.join(tree.xpath('//div[@class="panel-body"]//div[@data-label="Number of Seats"]//text()')).strip()
    transmission = ''.join(tree.xpath('//div[@class="panel-body"]//div[@data-label="Transmission"]//text()')).strip()
    cylinders = ''.join(tree.xpath('//div[@class="panel-body"]//div[@data-label="Number Of Cylinders"]//text()'))
    drive_type = ''.join(tree.xpath('//div[@class="panel-body"]//div[@data-label="Drive Type"]//text()')).strip()
    fuel = ''.join(tree.xpath('//div[@class="panel-body"]//div[@data-label="Fuel"]//text()')).strip()
    year = soup.find('small','mileage')
    if(year):
        year = soup.find('small','mileage').text.split()[0]
        mileage = soup.find('small','mileage').text.split()[2]
    else:
        year = 'Not given'
        mileage = "Not given"
    row.writerow([
        i,
        full_name,
        brand,
        model,
        model1,
        price,
        location,
        body_type,
        seats,
        transmission,
        cylinders,
        drive_type,
        fuel,
        year,
        'Used cars'  
    ])
    print(i)
    