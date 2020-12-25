from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html
import re
import csv
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'
f = open('123output_data.csv','w',encoding="utf-8",newline="")
fr = open('extra.txt','r').read().split('\n')
row = csv.writer(f)

def parsing_data(data):
	# r = s.get()
	r = s.get(i)
	tree = html.fromstring(r.text)
	product_name = ''.join(tree.xpath('//td[@class="title"]//text()')).strip()
	description = ''.join(tree.xpath('//p[contains(string(),"Standard Dimensions:")]//following-sibling::ul//li//text()')).strip().replace('\n','').replace('\t','')
	img = tree.xpath('//td[@class="psbody_r"]//div//p//img//@src')
	row.writerow([
		i,
		product_name,
		description,
		img
	])


for i in fr:
	parsing_data(i)
	print(i)