from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('style_links','r',encoding='utf-8').read().split('\n')
fw = open('style_data_123','w',encoding='utf-8')
last = 'page={}&sortOn=11&'
for i in fr:
    for j in range(1,50):
        m_url = i+last.format(j)
        r = s.get(m_url)
        soup = bs(r.content,'html.parser')
        a = soup.find_all('a','quickview-url')
        for k in a:
            fw.write('https://www.stylecraftonline.com'+k.get('href')+'\n')
        print(m_url)
        print(r.status_code)