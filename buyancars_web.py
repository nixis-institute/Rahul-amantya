# from bs4 import BeautifulSoup as bs
from requests import Session
# from lxml import html
import re
import csv
import json
from googletrans import Translator
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('buyanycar','r').read().split('\n')
fw = open('abishaya_data.csv','w',encoding='utf-8',newline="")
fm = open('missinigLinks','w',encoding='utf-8',newline="")
row = csv.writer(fw)
row1 = csv.writer(fm)
for i in fr[:5000]:
    try:
        r = s.get(i)
        js = json.loads(r.text)
        fuel = js['fuelType']
        brand = js['make']
        model = js['model']
        body_type = js['bodyType']
        transmission = js['transmission']
        price = js['price']
        city = js['city_name']
        mileage = js['mileage']
        drive_chain = js['inspectionReport']['general'][0]['fields'][14]['fieldValue']
        year = js['year']
        if(fuel.keys()=='name'):
            fuel = js['fuelType']
        else:
            fuel = 'Not given'

        if(brand):
            brand = js['make']['name']
        else:
            brand ='not given'

        if(model):
            model = js['model']['name']
        else:
            model ='Not given'
        
        if(body_type):
            body_type = js['bodyType']['name']
        else:
            body_type='Not given'

        if(transmission):
            transmission = js['transmission']['name']
        else:
            transmission= 'Not given'
        
        if(price):
            price = js['price']
        else:
            price = 'Not given'

        if(city):
            city = js['city_name']
        else:
            city = 'Not given'

        if(mileage):
            mileage = js['mileage']
        else:
            mileage = 'Not given'
        
        if(drive_chain):
            drive_chain = js['inspectionReport']['general'][0]['fields'][14]['fieldValue']
        else:
            drive_chain = 'Not given'

        if(year):
            year = js['year']
        else:
            year = 'Not given'
        row.writerow([
            i,
            brand,
            model,
            fuel,
            city,
            body_type,
            transmission,
            drive_chain,
            mileage,
            year,
            price,
            'Used cars'
        ])

        print(i)
    except:
        print('Exception!!')
        fm.writer(i)
        pass
        