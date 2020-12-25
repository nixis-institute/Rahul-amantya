from requests import Session
import re
import csv
s = Session()
s.headers["User-Agent"]='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
fr = open('all__.txt','r').read().split('\n')
fd = open('auto_data.csv',mode='w',encoding='utf-8',newline="")
row = csv.writer(fd)
for i in fr[:10]:
    r = s.get(i)
    if(re.search('<dt class="sc-ellipsis">Make</dt>\s<dd>\s(.*?)\s</dd>\s',r.text)):
        name = re.search('<dt class="sc-ellipsis">Make</dt>\s<dd>\s(.*?)\s</dd>\s',r.text).group(1)
    else:
        name = 'Not given'

    if(re.search('<dt class="sc-ellipsis">Model</dt>\s<dd>\s<a href="/lst/volkswagen/up%21" class="cldt-stealth-link">(.*?)</a>\s</dd>',r.text)):
        model = re.search('<dt class="sc-ellipsis">Model</dt>\s<dd>\s<a href="/lst/volkswagen/up%21" class="cldt-stealth-link">(.*?)</a>\s</dd>',r.text).group(1)
    else:
        model = 'Not given'

    if(re.search('<dt>First Registration</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/re_2017" class="cldt-stealth-link">(.*?)</a>\s</dd>',r.text)):
        regis = re.search('<dt>First Registration</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/re_2017" class="cldt-stealth-link">(.*?)</a>\s</dd>',r.text).group(1)
    else:
        regis = 'Not given'

    if(re.search('<dt class="sc-ellipsis">Type</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/ot_used" class="cldt-stealth-link">(.*?)</a>',r.text)):
        type_ = re.search('<dt class="sc-ellipsis">Type</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/ot_used" class="cldt-stealth-link">(.*?)</a>',r.text).group(1)
    else:
        type_ = 'Not given'

    if(re.search('<dt>Gearing Type</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/tr_manual" class="cldt-stealth-link">(.*?)</a>',r.text)):
        used = re.search('<dt>Gearing Type</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/tr_manual" class="cldt-stealth-link">(.*?)</a>',r.text).group(1)
    else:
        used = 'Not given'
    
    if(re.search('<dt class="sc-ellipsis">Fuel</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/ft_gasoline" class="cldt-stealth-link">(.*?)</a>',r.text)):
        fuel = re.search('<dt class="sc-ellipsis">Fuel</dt>\s<dd>\s<a href="/lst/volkswagen/up%21/ft_gasoline" class="cldt-stealth-link">(.*?)</a>',r.text).group(1)
    else:
        fuel = 'Not given'
    
    if(re.search('<dt>Drive chain</dt>\s<dd>\s(.*?)\s</dd>',r.text)):
        driv = re.search('<dt>Drive chain</dt>\s<dd>\s(.*?)\s</dd>',r.text).group(1)
    else:
        driv = 'Not given'
    
    if(re.search('<dt>Country version</dt>\s<dd>\s(.*?)\s</dd>',r.text)):
        coun = re.search('<dt>Country version</dt>\s<dd>\s(.*?)\s</dd>',r.text).group(1)
    else:
        coun = 'Not given'
    
    if(re.search('<div data-item-name="vendor-contact-city" class="sc-grid-col-12">(.*?)</div>',r.text)):
        add = re.search('<div data-item-name="vendor-contact-city" class="sc-grid-col-12">(.*?)</div>',r.text).group(1)
    else:
        add = 'Not given'
    row.writerow([
        name,
        model,
        regis,
        type_,
        used,
        fuel,
        driv,
        coun,
        add,
        i
    ])
    print(i)
    

    
