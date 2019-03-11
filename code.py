import requests
import json
import random
import string
p=[]
t=[]
f=open("all.txt")
fa=f.readlines()
for faa in fa:
    dsa=faa.split(" | ")
    p.append(dsa[0])
    t.append(dsa[1])
le=len(p)
for i in range(0,3105):
    r = requests.get('https://randomapi.com/api/')
    datas=r.text
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
    "Vertical": "Web",
    "Company": "",
    "Phone": phone,
    "g-recaptcha-response": "", 
    "RegistrationType": "Default",
    "PageUrl": "https://www.xxxxxxxxx.com/",
    "PageTitle": "xxxxxxxxx",
     }
    proxiesDict = {'http': 'http://163.172.48.109:15001','https': 'https://163.172.48.109:15001'}
    r = requests.post('https://www.xxxxxxxxx.com/api/account/create', data=datsa)
    data = json.loads(r.text)
    apikey=data["accountInfo"]["apiKey"]
    for k in range(0,10):
        try:
            ps=p[k].split("//")
            url='https://api.xxxxxxxxx.com/v1/site/'+ps[1]+'/technologies/pages?userkey='+apikey+'&techid='+str(t[k])+'&format=json'
            r = requests.get(url)
            dataa=r.text
            f=open("data.txt","a+")
            dff=str(t[k]+" | "+p[k]+" | "+dataa)
            f.write(dff)
            f.write("\n")
        except:
            f=open("data.txt","a+")
            dff=str(t[k]+" | "+p[k])
            f.write(t[k]+" | "+p[k])
            f.write("\n")
    p=p[10:]
    t=t[10:]
