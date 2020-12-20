from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
# car-first-registration
import time
fr = open('final_links.txt',mode='r',encoding='utf-8').read().split('\n')
fd = open('outputfiles.csv',mode='w',newline='')
row = csv.writer(fd)
driver = webdriver.Firefox()
for i in fr[1:500]:
    try:
        driver.get(i)
        driver.maximize_window() 
        time.sleep(15)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        soup = bs(driver.page_source,'html.parser')
        if(soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-production'})):
            year = soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-production'}).text
        else:
            year = 'Not given'
        
        if(soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-first-registration'})):
            year2 = soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-first-registration'}).text
        else:
            year2 = 'Not given'

        if(soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-mileage'})):
            mil = soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-mileage'}).text
        else:
            mil = 'Not given'

        if(soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-fuel'})):
            feul_t = soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-fuel'}).text
        else:
            feul_t = 'Not given'
        
        if(soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-transmission'})):
            trans = soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-transmission'}).text
        else:
            trans = 'Not given'
        
        if(soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-body'})):
            body = soup.find('div','rc-CarProfile').find('div',attrs={'data-attr':'car-body'}).text
        else:
            body = 'Not given'
        
        if(soup.find('a','uitest-address-link')):
            couty = soup.find('a','uitest-address-link').text
        else:
            couty = 'Not given'

        if(soup.find('h1','uitest-car-title')):
            brand = soup.find('h1','uitest-car-title').text.split()[0]
            model = soup.find('h1','uitest-car-title').text.split()[1]
            model2 = soup.find('h1','uitest-car-title').text.split()[2]

        else:
            name = 'Not given'
        
        row.writerow([
            year,
            year2,
            mil,
            feul_t,
            trans,
            body,
            couty,
            brand,
            model,
            model2,
            i
        ])
        print(i)
    except:
        pass
        print('Error......')
