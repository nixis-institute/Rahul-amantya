from requests import Session
import re
import csv
import time
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
fd = open('find_links.txt','r',encoding='utf-8').read().split('\n')
fr = open('all_data(1).csv','w',encoding='utf-8',newline='')
row = csv.writer(fr)

def scrap(i,t=1):
    time.sleep(t)    
    try:
        r = s.get(i)
        # soup = bs(r.content,'html.parser')
        if(re.search('<td class="nfo" data-spec="year">(.*?)</td>',r.text).group(1)):
            date = re.search('<td class="nfo" data-spec="year">(.*?)</td>',r.text).group(1).strip('|')
        else:
            date = 'Not given'
        if(re.search('<td class="nfo" data-spec="status">(.*?)</td>',r.text).group(1)):
            status = re.search('<td class="nfo" data-spec="status">(.*?)</td>',r.text).group(1).strip('/n')
        else:
            status = 'Not given'
        if( re.search('<h1 class="specs-phone-name-title" data-spec="modelname">(.*?)</h1>',r.text).group(1)):
            nam =  re.search('<h1 class="specs-phone-name-title" data-spec="modelname">(.*?)</h1>',r.text).group(1)
        else:
            nam ='Not given'
        # fr.write()
        row.writerow([
            nam,
            date,
            status,
            i
        ])
    except:
        pass
        print('exxeption......')
        scrap(i,5)    
    print(i)

for i in fd[71:1252]:
    scrap(i,0)    