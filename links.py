from bs4 import BeautifulSoup as bs
from requests import Session
s = Session()
s.headers['User-Agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
f = open('222all_links.txt','w',encoding='utf-8')
# l = []
l = ['Audi','BMW','Mercedes-Benz','Opel','Skoda','Volkswagen','Abarth','AC','Acura','Aixam','Alfa Romeo','ALPINA','Artega','Asia Motors','Aston Martin','Audi','Austin','Austin Healey','Bentley','BMW','Borgward','Brilliance','Bugatti','Buick','Cadillac','Casalini','Caterham','Chatenet','Chevrolet','Chrysler','Citroën','Cobra','Corvette','Cupra','Dacia','Daewoo','Daihatsu','DeTomaso','Dodge','Donkervoort','DS Automobiles','Ferrari','Fiat','Fisker','Ford','GAC Gonow','Gemballa','GMC','Grecav','Hamann','Holden','Honda','Hummer','Hyundai','Infiniti','Isuzu','Iveco','Jaguar','Jeep','Kia','Koenigsegg','KTM','Lada','Lamborghini','Lancia','Land Rover','Landwind','Lexus','Ligier','Lincoln','Lotus','Mahindra','Maserati','Maybach','Mazda','McLaren','Mercedes-Benz','MG','Microcar','MINI','Mitsubishi','Morgan','Nissan','NSU','Oldsmobile','Opel','Pagani','Peugeot','Piaggio','Plymouth','Polestar','Pontiac','Porsche','Proton','Renault','Rolls-Royce','Rover','Ruf','Saab','Santana','Seat','Skoda','Smart','speedART','Spyker','Ssangyong','Subaru','Suzuki','Talbot','Tata','TECHART','Tesla','Toyota','Trabant','Triumph','TVR','Volkswagen','Volvo','Wartburg','Westfield','Wiesmann','Autres']
url = 'https://www.automobile.fr/voiture/{}/vhc:car,pgn:{},pgs:10'

for lst in l:
    for i in range(1,7):
        m_url = url.format(lst,i)
        r = s.get(m_url)
        soup = bs(r.content,'html.parser')
        a = soup.find_all('a','vehicle-data track-event u-block js-track-event js-track-dealer-ratings')
        for data in a:
            f.write('https://www.automobile.fr/'+data.get('href')+'\n')
        print(m_url)
        print(r.status_code)
    # print(lst)
            # f.write('')
    # for i in range(1,7):
    #     for i in soup.find('select','form-control form-control--dropdown js-make-dropdown js-track-event').find_all('option'):
    #         l.append(i.text.replace('Tous','').replace('───────────────',''))
        # m_url = url.replace
        # for j in range(len(l)):