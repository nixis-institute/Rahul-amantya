from bs4 import BeautifulSoup as bs
from requests import Session
from lxml import html
import csv
import pandas as pd


s = Session()
s.headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
fr = open('working_links_set','r').read().split('\n')
fw = open('given_pawan.csv','w',encoding='utf-8')
row = csv.writer(fw)
output = []
for links in fr:
    r = s.get(links)
    features = ''
    add_information = ''
    srs = ''
    lst_data=''
    soup = bs(r.content,'html.parser')
    tree = html.fromstring(r.content)
    pr1 = ''.join(tree.xpath('//div[@class="prod-detail"]//span[@class="static_breadcrumb"]//strong//text()')).strip()
    pr2 = ''.join(tree.xpath('//span[@class="back_link"]//a//text()')).strip()
    product_name = ''.join(tree.xpath('//h2[@class="prod-content__title-cont--title"]//text()')).strip()
    price = ''.join(tree.xpath('//span[@class="prod-content__price-cont--price price_value"]/text()')).strip()
    # description = ''.join(tree.xpath('//div[@class="prod-content--description--content"]//p//text()')).strip()
    description = "".join(tree.xpath("//div[@class='prod-content__description']//p//text()")) + "".join(tree.xpath("//div[@class='prod-content__description']//li//text()"))
    
    description123= ''.join(tree.xpath('//div[@class="prod-content--description--content"]//text()')).strip().replace('\n','').replace('\r','').replace('\t','')
    ul_description = ' @|@ '.join(tree.xpath('//div[@class="prod-content--description--content"]//ul//li//text()')).strip().replace('\n','').replace('\t','').replace('\r','')
    select_data = ','.join(tree.xpath('//select[@id="id_Ecdv"]//option//text()')).strip().replace('----Please Select----','')
    series = soup.find('div','table__guide table__guide__scroll')
    div = soup.find('div','prod-content--description--content').find_all('div','table__guide')
    # print(len(div))

    tables = soup.find_all("div","table__guide")
    # for i in tables:
    #     if(i.find("th").text.find("Features")!=-1):
    
    if(tables):
        df = pd.read_html(r.text)
        
        loop = []
        spc_table = []
        add_info = []
        for i in df:
            if(list(i.keys()).count("Features") !=0):
                spc_table = i
            elif(list(i.keys()) == [0,1]):
                add_info = i
            else:
                loop = i
    else:
        loop = []
        spc_table = []
        add_info = []

    # list(df[0].keys()).count("Features")
    # for i in 
    # if(len(div)==3):
    #     if(div[0]):
    #         for i in div[0].find('tbody').find_all('tr'): 
    #             td1 = i.find_all('td')[0] 
    #             td2 = i.find_all('td')[1] 
    #             # print('{} @:@ {}'.format(td1.text.strip(),td2.text.strip().replace('\n','')))
    #             features+='{} @:@ {}|'.format(td1.text.strip(),td2.text.strip().replace('\n',''))
    #     else:
    #         features='Not given'

    #     if(div[1]):

    #         # for k in div[1].find_all('tr'): 
    #         #     td = k.find_all('td') 
    #         #     for l in td: 
    #         #         srs+= "{}|".format(l.text.strip().replace('\n','').replace('\r','').replace('\t',''))

    #         df = pd.read_html(r.text)
    #         srs = df[1].to_dict()

    #     else:
    #         srs='Not given'        
    
    #     if(div[2]):
    #         for j in div[2].find('tbody').find_all('tr'): 
    #             th = j.find('th') 
    #             td = j.find('td') 
    #             # print('{} @:@ {}'.format(th.text.strip(),td.text.strip()))
    #             add_information+='{} @:@ {}|'.format(th.text.strip(),td.text.strip())
    #     else:
    #         add_information='Not given'

    # elif(len(div)==2):
    #     if(div[0]):
    #         for l in div[0].find('tbody').find_all('tr'): 
    #             td1 = l.find_all('td')[0] 
    #             td2 = l.find_all('td')[1] 
    #             # print('{} @:@ {}'.format(td1.text.strip(),td2.text.strip().replace('\n','')))
    #             features+='{} @:@ {}'.format(td1.text.strip(),td2.text.strip().replace('\n',''))
    #     else:
    #         features='Not given'

    #     if(div[1]):
    #         for m in div[1].find('tbody').find_all('tr'): 
    #             th = m.find('th') 
    #             td = m.find('td') 
    #             # print('{} @:@ {}'.format(th.text.strip(),td.text.strip()))
    #             add_information+='{} @:@ {}'.format(th.text.strip(),td.text.strip())
    #     else:
    #         add_information='Not given'

    # else:
    #     print('Nothing')

    last_table = soup.find('div','table__guide table__guide__scroll')
    if(last_table):
        if(last_table):
            for k in div[1].find_all('tr'): 
                td = k.find_all('td') 
                for l in td: 
                    # print("{}|".format(j.text.strip().replace('\n','').replace('\r','').replace('\t','')))
                    lst_data+= "{}|".format(l.text.strip().replace('\n','').replace('\r','').replace('\t',''))
        else:
            lst_data='Not given'


    # if(series):    
    #     for k in soup.find('div','table__guide table__guide__scroll').find('tbody').find_all('tr'): 
    #         td = k.find_all('td') 
    #         for l in td: 
    #             # print("{}|".format(j.text.strip().replace('\n','').replace('\r','').replace('\t','')))
    #             srs+= "{}|".format(l.text.strip().replace('\n','').replace('\r','').replace('\t',''))
    # else:
    #     srs='Not given'
    img = ','.join(set(tree.xpath('//a[@class="main_img_link"]//@src'))).strip()

    
    # if(srs!="Not given"):
    if(len(loop)==0):
        d = {
            "url":links,
            "image":img,
            "pr1":pr1,
            "pr2":pr2,
            "product_name":product_name,
            "description":description,
            "price":price,
        }
        if(len(spc_table)):
            sc = dict(zip(spc_table["Features"],spc_table["Description"]))
            output.append(d)
            output.append(sc)
        else:
            output.append(d)


    for i in range(len(loop)):
        d = {
            "url":links,
            "image":img,
            "pr1":pr1,
            "pr2":pr2,
            "product_name":product_name,
            "description":description,
            "price":price,
        }
        
        ad = dict(zip(add_info[0],add_info[1]))
        if(len(spc_table)):
            sc = dict(zip(spc_table["Features"],spc_table["Description"]))
        else:
            sc = {}   
        d.update(sc)
        d.update(ad)
        d.update(loop.iloc[i].to_dict())
        output.append(d)

    print(links)


dfx = pd.DataFrame(output)

out_excel = open("out.csv","w", newline="",encoding="utf-8")
dfx.to_csv(out_excel,index=False)
