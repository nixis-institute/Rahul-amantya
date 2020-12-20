from bs4 import BeautifulSoup as bs
from requests import Session
# f = open('carused_jp.')
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
f = open('all_lnk12.csv','w',encoding='utf-8')
url = 'https://carused.jp/car-list?category_id={}&page={}'
l = [40,25,5,15,1,20,35,30,10]

for i in l:
    n =1
    while(True):
        r = s.get(url.format(i,n))
        if(r.status_code!=404):
            soup = bs(r.content,'html.parser')
            div = soup.find_all('div','listBlock')
            for j in div:
                a = j.find('a')
                dt = 'https://carused.jp{}|{}'.format(a.get('href'),i)
                f.write(dt+'\n')
                # print('https://carused.jp'+a.get('href'))
        else:
            break
        n+=1
        print(r.url)
    print(i)
        