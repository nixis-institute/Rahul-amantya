from bs4 import BeautifulSoup as bs
from requests import Session
import csv
from lxml import html
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('11000_style_data_123','r').read().split('\n')
fw = open('whole_data.csv','w',encoding='utf8',newline="")
row = csv.writer(fw)
for i in fr[:100]:
    r = s.get(i)
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    product_name = ''.join(tree.xpath('//div[@class="row columns title-col"]//h1//text()')).strip()
    breadcomes = '->'.join(tree.xpath('//div[@class="breadcrumbs"]//ul//li//text()')).strip()
    description = ''.join(tree.xpath('//div[@class="medium-6 columns"]//h5//text()')).strip()
    dc = dict(zip(tree.xpath('//section[@class="row description"]//div[@class="small-3 columns label-col"]//p//text()'),tree.xpath('//section[@class="row description"]//div[@class="small-9 columns info-col"]//p//text()')))
    img = ''.join(tree.xpath('//div[@class="img-wrap"]//img//@src')).strip()
    row.writerow([
        i,
        product_name,
        breadcomes,
        description,
        img,
        dc
    ])
    print(i)