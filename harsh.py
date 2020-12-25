from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
# f1 = open('cod.txt','r',encoding='utf-8').read().split('\n')
f2 = open('code1.txt','r',encoding='utf-8').read().split('\n')
f3 = open('out_data.csv','w',encoding='utf-8')
row = csv.writer(f3)
driver = webdriver.Firefox()
driver.get('https://catalog.noon.partners/en-ae/catalog')
for i in f2[:10]:
    # driver.get('https://catalog.noon.partners/en-ae/noon-catalog')
    inp = driver.find_element_by_xpath('//input[@placeholder="Search noon catalog"]')
    inp.send_keys(i)
    img = driver.find_element_by_xpath('//img[@alt="proImage"]')
    img.click()
    if(driver.find_element_by_class_name('rightView')):
        no = driver.find_element_by_xpath('//input[@type="text"]')
        no.send_keys(i)
        driver.find_element_by_class_name('btnCtr').find_element_by_class_name('primary').click()
        soup = bs(driver.page_source,'html.parser')
        ber_value = i.replace('N','').replace('A','')
        act = driver.find_element_by_class_name('primary')
        price = soup.find('span','').text.replace('AED ','')
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.send_keys(price)
        stock = driver.find_element_by_xpath('//input[@name="quantity"]')
        stock.send_keys('25')
        barcode = driver.find_element_by_xpath('//input[@placeholder="Enter barcode"]')
        barcode.send_keys(ber_value)
        for j in range(1,5):
            if(driver.find_element_by_class_name("inCtr").find_element_by_class_name("fixedBottom").find_element_by_tag_name("button")):
               driver.find_element_by_class_name("inCtr").find_element_by_class_name("fixedBottom").find_element_by_tag_name("button").click()
        row.writerow([
            i,
            ber_value,
            'completed'
        ])
            
    else:
        print(i,':- Available')