from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time 
# from selenium import org
# import org.openqa.selenium.JavascriptExecutor;
# f1 = open('cod.txt','r',encoding='utf-8').read().split('\n')
sku = open('white.csv','r',encoding='utf-8').read().split('\n')
pr = open('p_white.csv','r',encoding='utf-8').read().split('\n')
# f3 = open('out_data.csv','w',encoding='utf-8')
# row = csv.writer(f3)
# t = 1
driver = webdriver.Firefox()
driver.get('https://login.noon.partners/en/')
time.sleep(2)
emailElem = driver.find_element_by_name('email')
emailElem.clear()
emailElem.send_keys('Ringrowllc@gmail.com')  

password = driver.find_element_by_name('password')
# password.clear()
password.send_keys('Rabin@4321')

btn = driver.find_element_by_tag_name('button')
btn.click()

time.sleep(4)
# driver.get('https://catalog.noon.partners/en-ae/catalog')
# a = driver.find_elements_by_xpath('//li[@class = "jsx-2265404707 active app[object Object]"]')
# a[0].click()
# hovor.perform()
# driver.find_element_by_xpath("//a[contains(String() '/en-ae/noon-catelog')]")
# driver1.get('https://catalog.noon.partners/en-ae/noon-catalog')
# time.sleep(3)
for i,price in zip(sku[183:],pr[183:]):
        # driver1.get("https://catalog.noon.partners/en-ae/catalog/{}".format(i))
    driver.get("https://catalog.noon.partners/en-ae/noon-catalog/preview/{}".format(i))
    # driver.get("https://catalog.noon.partners/en-ae/noon-catalog/preview/N36611016A")
    # driver1.get('https://catalog.noon.partners/en-ae/noon-catalog/{}'.format(i))
    # driver1.get(i)
    time.sleep(6)
    soup = bs(driver.page_source,'html.parser')
    # if(soup.find('div','ctr')):
    se = driver.find_element_by_xpath('//input')
    # se.send_keys("N36611016A")
    se.send_keys(i)
    time.sleep(2)
    driver.find_element_by_class_name("primary").click()
    # driver.find_element_by_class_name("primary").click()
    # time.sleep(5)
    # driver.get('https://catalog.noon.partners/en-ae/catalog/{}'.format(i))
    # driver.get('https://catalog.noon.partners/en-ae/catalog/{}'.format(i))
    soup = bs(driver.page_source,'html.parser')
    time.sleep(5)
    # driver.execute_script("window.scrollTo(0,document.getElementByClassName('singleCtr').scrollHeight)")
    # driver.execute_script("document.getElementByClassName('singleCtr').scrollIntoView();")
    # driver.find_element_by_xpath('//input[@name="is_active"]').click()
    # p2 = []
    # for j in soup.find('div','highLowPriceCtr'):
    #     a = j.find_all('span','')[2]
    #     p2.append(a)
    # price = p2[1].text
    # if(driver.find_element_by_class_name("expandView").text.split()[3] == "25"):
    #     print(i)
    # else:
    driver.find_element_by_xpath('//input[@name="is_active"]').click()
    # for j in pr:
        # print(j)
    
    put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    put_value.send_keys(price)
    # for j in pr:
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.send_keys(j)
    
    # put_value.clear()
        # print(j)
    # driver.execute_script("window.scrollTo(0,document.getElementByClassName('singleCtr').scrollHeight)")
    # driver.execute_script("document.getElementByClassName('singleCtr').scrollIntoView();")
    stock = driver.find_element_by_xpath('//input[@name="quantity"]')
    stock.send_keys('25')
    # selenium.getEval("scrollBy(0, 250)");
    # JavascriptExecutor  = (JavascriptExecutor)driver;
    # jse.executeScript("window.scrollBy(0,250)");
    time.sleep(1)
    bar_code = (i).replace('A','').replace('N','')
    barcode = driver.find_element_by_xpath('//input[@placeholder="Enter barcode"]')
    time.sleep(1)
    barcode.send_keys(bar_code)
    button = driver.find_element_by_class_name('blue')
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    # while(driver.find_element_by_class_name('barcode').text != bar_code):
    #     time.sleep(1)
    #     bar_code = (i).replace('A','').replace('N','')
    #     barcode = driver.find_element_by_xpath('//input[@placeholder="Enter barcode"]')
    #     barcode.send_keys(bar_code)
    #     button = driver.find_element_by_class_name('blue')
    #     driver.execute_script("arguments[0].click();", button)
    # else:
    #     True
    # driver.find_element_by_class_name('blue').click()


    submit = driver.find_element_by_class_name("primary")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(2)
        # if(driver.find_element_by_class_name('localeStatus').text != "Live"):
        #     time.sleep(4)
        #     submit = driver.find_element_by_class_name("primary")
        #     driver.execute_script("arguments[0].click();", submit)
        # time.sleep(10)

        # driver.find_element_by_class_name("primary").click()
        # time.sleep(10)
        # driver.find_element_by_class_name("primary").click()

#     row.writerow([
#         i,
#         # ber_value,
#         'completed'
# ])
#  row.writerow([
#             i,
#             "Already Available"
#         ])   
