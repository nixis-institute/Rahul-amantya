from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
f = open('lnk.txt',mode='w',encoding='utf-8')
url = 'https://www.adesa.eu/en/findcar'
# while True:
driver = webdriver.Firefox()
driver.get(url)
try:
    for i in range(1,148):
        driver.maximize_window() 
        time.sleep(15)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # driver.implicitly_wait(20)
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        soup =  bs(driver.page_source,'html.parser')
        sec = soup.find_all('section','rc-CarCardDesktop')
        # print(sec[0]) 
        for j in sec:
            a = j.find('a')
            f.write('https://www.adesa.eu'+a.get('href')+'\n')
        btn = driver.find_element_by_xpath('//ul[@class="pagination"]//li[@class="next"]')
        btn.click()
        print(i)
except:
    pass
    print('Error....')
