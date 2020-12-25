from requests import Session
from bs4 import BeautifulSoup as bs 
from lxml import html
import csv
import re
# import random
import time
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'
f = open('outputfile_10.csv','w',encoding='utf-8',newline="")
url = "https://www.amazon.in/s?k=beauty+products&i=beauty&page={}"
row = csv.writer(f)
l = []
for i in range(1,5):
	r = s.get(url.format(i))
	if(r.status_code==200):
		tree = html.fromstring(r.text)
		lnk = re.findall('<a class="a-link-normal a-text-normal" target="_blank" href="(.*?)">',r.text)
		# print(lnk)
		for j in lnk:
			n = "https://www.amazon.in{}".format(j)
			print(n)
			l.append(n)
			# row.writerow([l])
		# print(r.status_code)
		print(r.url)
	# print(l)
# print(l)
print('\n')
print('And now print Links...............................................')
print('\n')
time.sleep(5)
for links in list(set(l)):
	r = s.get(links)
	print(r.url)
	# print(r.status_code)
	if(r.status_code!=404):
		tree = html.fromstring(r.text)
		brand = ''.join(tree.xpath('//th[@class="a-color-secondary a-size-base prodDetSectionEntry" and contains(string(),"Brand")]//following-sibling::td//text()'))
		if(brand):
			brand = ''.join(tree.xpath('//th[@class="a-color-secondary a-size-base prodDetSectionEntry" and contains(string(),"Brand")]//following-sibling::td//text()')).split()[0]
		else:
			brand = "Not given"
		product_name = ''.join(tree.xpath('//span[@class="a-size-large product-title-word-break"]//text()')).strip().replace('(Renewed) ','')
		price = ''.join(tree.xpath('//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]//text()')).strip().replace('鈧孤','')
		stock = ''.join(tree.xpath('//span[@class="a-size-medium a-color-success"]//text()')).strip()
		ASIN = ''.join(tree.xpath('//th[@class="a-color-secondary a-size-base prodDetSectionEntry" and contains(string(),"ASIN")]//following-sibling::td//text()')).strip()
		ratings = re.search('<span class="a-icon-alt">(.*?)</span></i>',r.text)
		if(ratings):
			ratings = re.search('<span class="a-icon-alt">(.*?)</span></i>',r.text).group(1)
		else:
			ratings= "Not given"
		row.writerow([
			r.url,
			brand,
			product_name,
			price,
			stock,
			ASIN,
			ratings
			])
		print("Status code is {}".format(r.status_code))
		print("Links :- {}".format(r.url))
	# print("404 links{}".format(links))