from bs4 import BeautifulSoup as bs
from requests import Session
import csv
import re
# save from yoututbe and a music Roudeep - Baby You (Original Mix)
s = Session()
f = open('autodata24.csv.csv',mode='w',encoding='utf-8',newline='')
fr = open('used_audi.txt',mode='r',encoding='utf-8')
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
row = csv.writer(f)
rd = fr.read().split()
l = 1
for i in rd:
    try:
        r = s.get(i,headers=headers)
        nm = ''
        pr = ''
        n1 = ''
        n2 = ''
        n3 = ''
        n4 = ''
        nc = ''
        a = ''
        soup = bs(r.content,'html.parser')
        # name = soup.find('span','cldt-detail-makemodel sc-ellipsis')
        prce = soup.find('div','cldt-price').find('h2').text.strip().replace('.-','').replace('€ ','').replace(',','')
        # if(name):
        #     nm += soup.find('span','cldt-detail-makemodel sc-ellipsis').text+'|'
        # else:
        #     nm = "Not given|"
        if(prce):
            pr += prce
        else:
            pr = 'Not given'

        left = soup.find_all("div","cldt-categorized-data cldt-data-section sc-pull-left")
        if(len(left) == 2):
            # ky1 = [a.text.strip() for a in left[0].find_all('dt')]
            # val1 = [b.text.strip() for b in left[0].find_all('dd')]
            k1 = [c.text.strip() for c in left[1].find_all('dt')]
            v1 = [d.text.strip() for d in left[1].find_all('dd')]
            # for x,y in zip(ky1,val1):
            #     n1 += "{}:{}|".format(x,y)
            for k,j in zip(k1,v1):
                n2 += "{}:{}|".format(k,j)
        # else:
        #     n1 = 'Not given'
        #     n2 = 'Not given'
        #     n3 = "Not given"
        right = soup.find("div","cldt-categorized-data cldt-data-section sc-pull-right")
        if(right):
            keys1 = [e.text.strip() for e in right.find_all('dt')]
            values1 = [i10.text.strip() for i10 in right.find_all('dd')]
            for f,g in zip(keys1,values1):
                n3 += "{}:{}|".format(f,g)

        # grid = soup.find('div','cldt-data-section sc-grid-col-s-12')
        # if(grid):
        #     dt = [i1.text.strip() for i1 in grid.find_all('dt')]
        #     dd = [i2.text.strip() for i2 in grid.find_all('dd')]
        #     for d1,d2 in zip(dt,dd):
        #         n4 += '{}:{}|'.format(d1,d2)
        
        hp = soup.find('span','sc-font-m cldt-stage-primary-keyfact')
        if(hp):
            hour = soup.find('span','sc-font-m cldt-stage-primary-keyfact').text.strip()
        else:
            hour = 'Not given'

        if(soup.find('div','cldt-data-section sc-grid-col-s-12').find_all('div')):
            ct = soup.find('div','cldt-data-section sc-grid-col-s-12').find_all('div')
            for p1 in ct:
                    nc+= p1.text.strip().replace(',','').replace('\t','').replace('\r','').replace('\n','')+'|'
        else:
            nc+= 'Not given'

        if(soup.find('div','cldt-data-section sc-grid-col-s-12').find('a','cldt-stealth-link')):
            a+= soup.find('div','cldt-data-section sc-grid-col-s-12').find('a','cldt-stealth-link').text.strip().replace(',','').replace('\t','').replace('\r','').replace('\n','')
        else:
            a+='Not given'

        if(re.search('<div data-item-name="vendor-contact-city" class="sc-grid-col-12">(.*?)</div>',r.text).group(1)):
            place = re.search('<div data-item-name="vendor-contact-city" class="sc-grid-col-12">(.*?)</div>',r.text).group(1)
        else:
            place = 'Not given'
        # all1 = '{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(nm,pr,n1,n2,n3,hour,nc,a,i)
        # f.write(all1+'\n')
        # print(n1)
        # print(n2)
        # print(n3)
        row.writerow([
            # nm,
            place,
            pr,
            hour,
            # n1,
            n2,
            n3,
            # n4,
            '|Feul:'+a+'|',
            '|'+nc,
            i
        ])
        print(i)
        print(l)
        l+=1
    except:
        pass
        print('Exceptions.....')

