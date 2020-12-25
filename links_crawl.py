from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
import re
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fw = open('moter3','w',encoding='utf-8',newline="")
# fr = open('all_lnks','r',encoding='utf-8',newline="").read().split('\n')
url = 'https://www.power-sonic.com/powersport/atvs-quads/page/{}/'
for i in range(1,14):
    r = s.get(url.format(i))
    soup = bs(r.content,'html.parser')
    a = soup.find_all('a','text-center mainbtn')
    for j in a:
        # print(j)
        if(j):
            fw.write(j.get('href')+'\n')

    print(url.format(i))



# for i in fr[:10]:
#     bk = 'page/{}/'
#     # m_url = i+'page/{}/'
#     n=1
#     while True:
#         m_url = i+bk.format(n)
#         r = s.get(m_url)
#         soup = bs(r.content,'html.parser')
#         a = soup.find_all('a','relatedproducts__itemfullclick')
#         if(a):
#             for lnk in a:
#                 fw.write(lnk.get('href')+'\n')
#                 # n+=1
#             print(m_url)
#         else:
#             break
#         n+=1
