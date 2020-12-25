#Automation for checking that product is Active or Not in Site
# It's Current Price

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
# row = writerow()
check_data = open('rs_trader1.csv','r',encoding='utf-8').read().split('\n')
f4 = open('not_act1.csv','w',encoding='utf-8')

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
for i in check_data[0:18]:
    i = i.split(",")
    driver.get('https://catalog.noon.partners/en-ae/catalog/')
    time.sleep(4)
    search = driver.find_element_by_xpath('//input[@placeholder="Search Catalog"]')
    search.send_keys(i[1])
    # os.system('clear')
    time.sleep(3)
    soup = bs(driver.page_source,'html.parser')
    # img = driver.find_element_by_xpath('//img[@alt="blank"]')
    # if(driver.find_element_by_class_name("expandView").text.split()[3] == "25"):
    #     print("Not Found"
    #     )

    try: 
        driver.find_element_by_xpath('//img[@alt="blank"]')
        time.sleep(4)
        row.writerow(i[1] + '\n')
    except:
        # driver.find_element_by_xpath('//div[@class="not_live"]').text
        # driver.find_element_by_class_name('jsx-182793294').text
        nota = soup.find('div','statusCtr').text
        # if(nota == "Live"):
        #     True
        # else:    
            # curr_pr = driver.find_element_by_xpath('//div[@class="jsx-448933760"]').text.replace('AED','')
        curr_pr = soup.find('span','').text.replace('AED','')
        f4.write(i[1]+','+ curr_pr + ','+ nota + '\n')

        # row.writerow(i)
        # print('NOt Active............................')
    print(i[1])