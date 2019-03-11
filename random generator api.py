import requests
import json
import random
import string
rs = requests.get('https://randomapi.com/api/6de6abfedb24f889e0b5f675edc50deb?fmt=raw&sole')
datas=rs.text
d=datas.split("},")
da=d[0]
da=da[1:]
da=da+"}"
da=json.loads(da)
phone=''.join([random.choice(string.digits) for n in range(8)])
datsa={   
    "FirstName": da['first'],
    "LastName": da['last'],
    "Email": da['email'],
    "GeneratePassword": "true",
    "Vertical": "Web Hosting",
    "Company": "",
    "Phone": phone,
    "g-recaptcha-response": "",
    "recaptchaToken": "03AL4dnxrryMSSrq9YOevM7Hit7IubrRGCNAAvdiDGPZfCXtMRkYXERssxNkM_6U-Jaus7vj3e9JG5hvzdTaa9h-UqZilJZk3XswUp-rKJ_ke00qRPgUFcJHQZHAVCj_BBBgPTle0iQHRsULOwMZ51GuzJ3ObGFT7145npbbwAAbe1O6AxtGfoSWiJ-gl3qdNpKtHZer_aIR6-Xd4zAqbOwsop1O27RPGxUYB3DeznfJ2MoBomxdhItfj4-hHvKwTiTO3fZb82pnCMWXfwuYC8Dt8KaSxdpOJ92w",
    "RegistrationType": "Default",
    "PageUrl": "https://www.similartech.com/",
    "PageTitle": "Generate Sales Leads with Web Technology Stack Lookup | SimilarTech",
     }

sessionid=str(random.random())
url='https://www.similartech.com/api/account/create'
rheaders={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "X-Request-Verification-Token":"ptx3abludWztKE_iQFBbHhlslHQYB4nimy5FFpY5xVecvY5S8agrSFqp3kne4hbzhGxGtxPVe0tuk3YWZW2Zp6rhnu41"
    }
proxiesDict = {'http': 'http://lum-customer-hl_c55bdafb-zone-zone1-session-'+str(sessionid)+':23pjgccxltzn@zproxy.lum-superproxy.io:22225',
                   'https': 'https://lum-customer-hl_c55bdafb-zone-zone1-session-'+str(sessionid)+':23pjgccxltzn@zproxy.lum-superproxy.io:22225',}
rheaders={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36','referer':url}
r = requests.get("https://www.google.com/recaptcha/api2/bframe?hl=en&v=v1537770717608&k=6LddGUkUAAAAAPTls3na6IR-rM9L34XwlsmjzLkr")
print(r,r.text)


        
