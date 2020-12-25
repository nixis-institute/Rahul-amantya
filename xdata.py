from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import random
#driver = webdriver.Firefox(executable_path=r'C:\Users\Hp\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
driver = webdriver.Firefox()
f = open("original_data.txt").read().split("\n")
out = open("original.csv","w")
count = 0
# for i in f[0:100]:
def scrap(i,t=1):
    try:
        time.sleep(t)
        driver.get(i)
        soup = bs(driver.page_source,'html.parser')
        # count = count + 1
        # print("______________________________________________"+str(count)+"______________________________________________")
        
        # l= [i.find('strong').text for i in soup.find_all("div","sellerDetails")
        if([i.text for i in soup.find_all("strong","jsx-2119389001")].count("Digital Upward")==0):

            if(soup.find("span","lowestPrice")==None):
                #True
                sellers = "No"
                # price_freeze = ""
                express = "No"
                last_price = float(soup.find("span","sellingPrice").find("span","value").text) 
                category = [i.text for i in soup.find_all("span","crumb")][-2]
                sub_category = [i.text for i in soup.find_all("span","crumb")][-1]
                # name = soup.find('div','coreWrapper').findAll('h1')[0].text
                out.write('{}|{}|{}|{}|{}|{}\n'.format(i,last_price,sellers,express,category,sub_category))
                url = ""
            else:
                price1 = float(soup.find("span","sellingPriceContainer").find("span","value").text)
                
                price2 = float(soup.find("span","lowestPrice").find("span","value").text) if soup.find("span","lowestPrice").find("span","value").text else 0 

                if price1<price2:
                    last_price = price1
                # elif(soup.find("span","cta")==None):
                #     last_price= price1
                else:
                    last_price = price2
                # l= [i.find('strong').text for i in soup.find_all("div","sellerDetails")]
                # url = i
                # for i in range(len(l)):
                #     if(l[i]=="Digital Upward"):
                #         url = ""

                sellers = int(soup.find("div","panelContainer").text[:2])
                prices = [i.find("span","value").text for i in soup.find_all("span","sellingPrice")]
                # del prices[0]
                # prices = prices[:sellers]
                # if (set(prices)==1):
                #     price_freeze= "Yes"
                # else:
                #     price_freeze = "No"

                
                if(soup.find("div","panel").find("img","fbn")):
                    express = "Yes"
                else:
                    express = "No"

                category = [i.text for i in soup.find_all("span","crumb")][-2]
                sub_category = [i.text for i in soup.find_all("span","crumb")][-1]
                # category = [i.text for i in soup.find_all("span","crumb")]
                # name = soup.find('div','coreWrapper').findAll('h1')[0].text
                # if(url==""):
                #     True
                # else:
                out.write('{}|{}|{}|{}|{}|{}\n'.format(i,last_price,sellers,express,category,sub_category))
        # out.write('{}|{}\n'.format(i,name))

    except:
        pass
        print(i)
for i in f[0:1000]:
    n = random.randint(1,10)
    scrap(i,n)
    count = count + 1
    print("______________________________________________"+str(count)+"______________________________________________")
