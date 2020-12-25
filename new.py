# Automation for First time Price Update

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

all_data = open('rs_trader1.csv','r',encoding='utf-8').read().split('\n')

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

for i in all_data[18:50]:
    i = i.split(",")
    driver.get("https://catalog.noon.partners/en-ae/catalog/{}".format(i[1]))
    soup = bs(driver.page_source,'html.parser')
    time.sleep(5)
    if(float(i[3]) == float(i[5]) and float(i[5])>float(i[4])):
        update_Price = float(i[5]) - 0.5
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()           
        put_value.send_keys(str(update_Price))
        time.sleep(2)
    elif(float(i[5])>float(i[3]) and float(i[5])>float(i[4])):
        update_Price = float(i[3]) - 0.2
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()
        put_value.send_keys(str(update_Price))
        time.sleep(2)    
    elif(float(i[5])>float(i[3]) and float(i[5])>float(i[4]) and 5<float(i[6]) and float(i[6])<10):
        # print("hdshdiski nj")
        update_Price = float(i[5]) - 0.5
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()
        put_value.send_keys(str(update_Price))
        time.sleep(2)
    elif(float(i[5])>float(i[3]) and float(i[5])>float(i[4]) and float(i[6])<5):
        update_Price = float(i[5]) - 0.5
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()
        put_value.send_keys(str(update_Price))
        time.sleep(2)
    elif(float(i[5])<float(i[4])):
        update_Price = float(i[4])
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()
        put_value.send_keys(str(update_Price))
        time.sleep(2)
        
    elif(float(i[5])<float(i[3]) and float(i[5])>float(i[4])):
        update_Price = float(i[5]) - 0.5
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()
        put_value.send_keys(str(update_Price))        
        time.sleep(2)
    # elif(float(i[5])>float(i[4]) and float(i[3])>float(i[4])):
    #     update_Price = float(i[3]) - float(0.2)
    #     print(update_Price)
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    else:
        True
    # time.sleep(2)
    submit = driver.find_element_by_class_name("primary")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(2)
    print(i[1])
    # driver.find_element_by_xpath('//a[@target="_blank"]').click()
    # if(driver.find_element_by_xpath('//p[@class="notAvailableNote"]').text):
    #     # if(float(i[3]) == float(i[5])):
    #     update_Price = update_Price + 0.5
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    #     # print(update_Price)
    # else:
    #     print("active.................")
    #     True
