from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
f = open('used_alpina.txt',mode='w',encoding='utf-8')
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
# url = 'https://www.autoscout24.com/lst/?sort=standard&desc=0&fuel=3&ustate=N%2CU&size=20&page={}&atype=C&'
url = 'https://www.autoscout24.com/lst/alpina?sort=standard&desc=0&offer=U%2CD%2CJ%2CO&ustate=N%2CU&size=20&page={}&atype=C&'
for i in  range(1,21):
    m_url = url.format(i)
    r = s.get(m_url,headers=headers)
    soup = bs(r.content,'html.parser')
    a = soup.find_all('div','cldt-summary-titles')
    for j in a:
        aa = j.find('a')
        f.write('https://www.autoscout24.com'+aa.get('href')+'?cldtidx=1&cldtsrc=listPage'+'\n')
    print(m_url)