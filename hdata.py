from requests import Session
import re
import time
s = Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
out = open("happy(201-250).csv","w")
f = open("all_link(1).txt","r").read().split("\n")

def scrap(i,t=1):
    time.sleep(t)
    try:
        r = s.get(i,proxies={"https":"http://scraperapi.render=true:a6438ab03fee3e0af7053fbbcaa5c20c@proxy-server.scraperapi.com:8001"},verify=False)
        ex = re.search("noon-express",r.text)
        # ex = re.search("https://k.nooncdn.com/s/app/2019/noon-bigalog/472711e386dd707b927b9b7c1b43fb6e190ea5c4/static/images/noon-express-en.png",r.text)
        if(ex):
            ex = "Yes"
        else:
            ex = "No"
        of = re.search('<h3 class="jsx-2803595502 ">(.*?)Offers Available</h3>',r.text)
        if of:
            offer = of.group(1)
        else:
            offer = 1
        printPrice = 0
        p1 = re.search('riceCurrency":"AED","price":(.*?),',r.text).group(1)
        p2 = re.search('tPrice"><span><span class="currency null">AED</span> <span class="value">(.*?)</',r.text)
        if(p2):
            p2 = p2.group(1)
            if(p1>p2):
                printPrice = p2
            else:
                printPrice = p1
        else:
            printPrice = p1


        out.write("{}|{}|{}|{}\n".format(r.url,ex,printPrice,offer))
        time.sleep(4)
        print(r.url)
    except:
        print("exception.....")
        scrap(i,2)




for i in f[200:250]:
    scrap(i,2)