from bs4 import BeautifulSoup as bs
from requests import Session
fw = open('sedan.txt','w',encoding='utf-8')
s = Session()
suv = 'https://www.beforward.jp/stocklist/page={}/sortkey=n/veh_type=4'
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
l = ['SUV','Truck','Pick up','Van','Sedan','Bus','Mini Van','Hatchback','Coupe','Convertible','Wagon','Mini Bus','Machinery','Forklift','Tractor''Tractor Head']
# for j in l:
for i in range(1,394):
    r = s.get(suv.format(i))
    soup = bs(r.content,'html.parser')
    p = soup.find_all('p','make-model')
    for j in p:
        a = j.find('a')
        fw.write('https://www.beforward.jp'+a.get('href')+'\n')
    print("number :- {}".format(i))
    print('url :- {}'.format(r.url))
# t = 'https://www.beforward.jp/stocklist/veh_type=9/sortkey=n'
# s = 'https://www.beforward.jp/stocklist/veh_type=6/sortkey=n'
# p = 'https://www.beforward.jp/stocklist/veh_type=7/sortkey=n'
# v = 'https://www.beforward.jp/stocklist/veh_type=8/sortkey=n'

