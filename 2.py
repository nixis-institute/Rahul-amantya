# Automation for First time Price Update
# For DIgital Upward

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

all_data = open('digi(-10)(24 oct).csv','r',encoding='latin-1').read().split('\n')
# price = open('digital(21 oct)406.csv','w',encoding='utf-8')
price = open('1digital350(24 oct).csv','w',encoding='utf-8')
driver = webdriver.Firefox()
driver.get('https://login.noon.partners/en/')
time.sleep(2)
emailElem = driver.find_element_by_name('email')
emailElem.clear()
emailElem.send_keys('gennextprollc@gmail.com')  

password = driver.find_element_by_name('password')
# password.clear()
password.send_keys('Vipul@987')

btn = driver.find_element_by_tag_name('button')
btn.click()
time.sleep(4)

# for i in all_data[500]:
# for i in all_data[405:]:    
for i in all_data[359:400]:    
    i = i.split(",")
    driver.get("https://catalog.noon.partners/en-ae/catalog/{}".format(i[1]))
    soup = bs(driver.page_source,'html.parser')
    time.sleep(10)
    if(float(i[5])>float(i[4])):
        update_Price = float(i[5]) - 0.1
        print('1')
        print(update_Price)
        put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
        put_value.clear()
        put_value.send_keys(str(update_Price))
        time.sleep(2)
    else:
        True
        print('2')
    # if(float(i[5])>=float(i[3]) and float(i[5])>float(i[4]) and float(i[4])>=float(i[3]) or float(i[4])==float(i[5])):
    #     update_Price = float(i[4])
    #     print(update_Price)
    #     print("new")
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    #     time.sleep(2)   
    # elif(float(i[5])>float(i[3]) and float(i[5])>float(i[4])):
    #     update_Price = float(i[3]) - 0.2
    #     print(update_Price)
    #     print("2")
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    #     time.sleep(2)    
    # elif(float(i[5])>float(i[3]) and float(i[5])>float(i[4]) and 5<float(i[6]) and float(i[6])<10):
    #     # print("hdshdiski nj")
    #     update_Price = float(i[5]) - 0.5
    #     print(update_Price)
    #     print("3")
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    #     time.sleep(2)
    # elif(float(i[5])>float(i[3]) and float(i[5])>float(i[4]) and float(i[6])<5):
    #     update_Price = float(i[5]) - 0.5
    #     print(update_Price)
    #     print('4')
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    #     time.sleep(2)
    # elif(float(i[5])<float(i[4])):
    #     update_Price = float(i[4])
    #     print(update_Price)
    #     print("5")
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))
    #     time.sleep(2)
        
    # elif(float(i[5])<float(i[3]) and float(i[5])>float(i[4])):
    #     update_Price = float(i[5]) - 0.5
    #     print(update_Price)
    #     print("6")
    #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    #     put_value.clear()
    #     put_value.send_keys(str(update_Price))        
    #     time.sleep(2)
    # # elif(float(i[5])>float(i[4]) and float(i[3])>float(i[4])):
    # #     update_Price = float(i[3]) - float(0.2)
    # #     print(update_Price)
    # #     put_value = driver.find_element_by_xpath('//input[@name="price_ae"]')
    # #     put_value.clear()
    # #     put_value.send_keys(str(update_Price))
    # else:
    #     True
    #     print('7')
    # time.sleep(2)
    submit = driver.find_element_by_class_name("primary")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(2)
    print(i[1])
    price.write(i[1]+','+str(update_Price) + '\n')

