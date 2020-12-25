from lxml import html
from requests import Session
from bs4 import BeautifulSoup as bs
import csv
import re
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0' 
fr = open('final_links','r').read().split('\n')
fw = open('58data.csv','w',encoding='utf-8',newline='')
row = csv.writer(fw)
for lnk_resq in fr[58:]:
    access=''
    spec = ''
    product_ = ''
    apple = ''
    l = []
    r = s.get(lnk_resq)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    if(re.search('class = "title" >(.*?)</a>',r.text)):
        name = re.search('class = "title" >(.*?)</a>',r.text).group(1)
    else:
        name = 'not found'

    f1img = 'http://www.steinel.net'+''.join(tree.xpath('//div[@class="heat_bar"]//img//@src'))
    f2img = 'http://www.steinel.net'+''.join(tree.xpath('//span[@class="text"]//@src'))
    des1 = ''.join(tree.xpath('//span[@class="Text"]//text()')).strip().replace('\n','').replace('\t','').replace('\r','')
    des2 = tree.xpath('//span[@class="text"]//div//text()')
    des3 = ''.join(tree.xpath('//span[@class="text"]//ul//li//text()')).strip().replace('\n','').replace('\t','').replace('\r','') 
    breads = '->'.join(tree.xpath('//span[@class="Breads"]//a//text()'))
    if(soup.find('div','product_buttons')):
        for other_links in soup.find('div','product_buttons').find_all('a'):
            l.append(other_links.get('href'))
        
        if(l[0]):
            respon = s.get(l[0])
            tab = bs(respon.content,'html.parser')
            table = tab.find("table",attrs={"bordercolor":"#c5c6c8"})
            if(table):
                for i in table.find_all('tr'):
                    td1 = i.find_all('td')[0] 
                    td2 = i.find_all('td')[1] 
                    # print('{}@:{}'.format(td1.text.strip().replace('            ',''),td2.text.strip().replace('            ',''))+'|')
                    spec+='{}@:{}'.format(td1.text.strip().replace('            ',''),td2.text.strip().replace('            ',''))+'|'
            else:
                spec='Not given'

        if(l[1]):
            rsp = s.get(l[1])
            acc = bs(rsp.content,'html.parser')
            if(acc.find('table',attrs={'width':'500'})):
                # if()
                for k in acc.find('table',attrs={'width':'500'}).findAll('td'): 
                    if(len(k.text.strip())): 
                        # print('{},'.format(i.text.strip().replace('\n','')))
                        access += "{},".format(k.text.strip())
            else:
                access = 'Not given'
        else:
            access = "Not Given"
        # application = bs(rqp.content,'html.parser')
        if(l[2]):
            rqp = s.get(l[2])
            tre = html.fromstring(rqp.content)
            apple = tre.xpath('//table[@style="width: 100%"]//tr//span//text()')
        else:
            apple ='Not given'
    else:
        product_ = 'Not found'
    row.writerow([lnk_resq,name,f1img,f2img,des1,des2,des3,breads,spec,access,apple,product_])
    print(lnk_resq)
