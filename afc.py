from bs4 import BeautifulSoup as bs
from lxml import html
from requests import Session
import csv
import re
s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0' 
fr = open('afcweb','r').read().split('\n')
fw = open('outputfile.csv','w',encoding='utf-8',newline='')
row = csv.writer(fw)
for i in fr[:50]:
    r = s.get(i)
    features_benefits = ''
    application = ''
    description = ''
    refrence_ratings = ''
    p_data = ''
    Temperature_Rating = ''
    grounding = ''
    marking = ''
    perefrence = ''
    ul_tag = ''
    description=""
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    product_name = ''.join(tree.xpath('//div[@class="inner_container"]//h1//span//text()')).strip()
    overview = ''.join(tree.xpath('//div[@class="entry-content"]//ul[@id="product-tabs"]/li//a[contains(string(),"Overview")]//text()')).strip()
    breedcomes = ''.join(tree.xpath('//div[@class="inner_container"]//ul[@class="breadcrumb"]//span//text()')).strip()
    spec = ''.join(tree.xpath('//div[@class="entry-content"]//ul[@id="product-tabs"]/li//a[contains(string(),"Specifications")]//text()')).strip()
    if(overview == 'Overview'):
        r = s.get(i+'#'+overview+'2')
        img = tree.xpath('//div[@id="overview1"]//div[@class="row"]//div[@class="col-lg-4 col-md-4 col-sm-4 col-xs-12 col-lg-push-8 col-md-push-8 col-sm-push-8 col-xs-push-0 text-center bottom20"]//a//@src')
        p_data = ''.join(tree.xpath('//div[@id="overview1"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//p//text()')).strip().replace('\n','')
        features_benefits = ','.join(tree.xpath('//div[@id="overview1"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//ul//text()')).strip().replace('\n','')  +''.join(tree.xpath('//div[@id="overview1"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//p//text()')).strip().replace('Properties:Note: Gray available upon request','')
        application = ''.join(tree.xpath('//div[@id="overview1"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[@id="applications"]//following-sibling::p//text()')).strip()
   
    if(spec == 'Specifications'):
        # spec = ''.join(tree.xpath('//div[@class="entry-content"]//ul[@id="product-tabs"]/li//a[contains(string(),"Specifications")]//text()')).strip()
        r = s.get(i+"#"+spec+"1")
        img = tree.xpath('//div[@id="overview1"]//div[@class="row"]//div[@class="col-lg-4 col-md-4 col-sm-4 col-xs-12 col-lg-push-8 col-md-push-8 col-sm-push-8 col-xs-push-0 text-center bottom20"]//a//@src')
        Temperature_Rating = ''.join(tree.xpath('//div[@id="specifications2"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[contains(string(),"Temperature Rating")]//following-sibling::ul//li//text()')).strip()
        # ref = ''.join(tree.xpath('//div[@id="specifications2"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[contains(string(),"References & Ratings")]//following-sibling::ul//li//text()')).strip()
        grounding = ''.join(tree.xpath('//div[@id="specifications2"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[contains(string(),"Grounding")]//following-sibling::p//text()')).strip()
        marking = ''.join(tree.xpath('//div[@id="specifications2"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[contains(string(),"Markings")]//following-sibling::p//text()')).strip()
        perefrence = ''.join(tree.xpath('//div[@id="specifications2"]//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[contains(string(),"Performance Tests")]//following-sibling::p//text()')).strip()
        ul_tag = tree.xpath('//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//ul//li//text()')
        description = ''.join(tree.xpath('//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[@id="description"]//following-sibling::dl//text()')).strip().replace('\n','|:')
        refrence_ratings = ''.join(tree.xpath('//div[@class="col-lg-8 col-md-8 col-sm-8 col-xs-12 col-lg-pull-4 col-md-pull-4 col-sm-pull-4 col-xs-pull-0"]//h4[@id="referencesratings"]//following-sibling::ul//text()')).strip()

    print(overview)
    print(spec)
    print(p_data)
    # print(features_benefits)
    # print(application)
    # print(description)
    # print(refrence_ratings)
    row.writerow([
        i,
        img,
        product_name,
        breedcomes,
        p_data,
        features_benefits,
        application,
        description,
        Temperature_Rating,
        refrence_ratings,
        grounding,
        marking,
        perefrence,
        ul_tag
        # i
    ])
    print(i)