import requests
import dns.resolver
import socket
import subprocess
import json
domain="stackoverflow.com"
with open("sitedetails.txt", "w", encoding="utf-8") as g:
    cmd="ping "+domain
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = process.communicate()
    out=str(out)
    out=(out.split('['))[1].split(']')[0]
    g=open("sitedetails.txt","a+")
    g.write("--- SITE NAME START ---")
    g.write("\n")
    g.write(domain)
    g.write("\n")
    g.write("--- SITE NAME END ---")
    g.write("\n\n")
    nameservers = dns.resolver.query(domain,'NS')
    g.write("--- NAME SERVERS START ---")
    g.write("\n")
    for data in nameservers:
        data=str(data)
        g.write(data)
        g.write("\n")
    g.write("--- NAME SERVERS END ---")
    g.write("\n\n")    
    #g.write(socket.gethostbyname(domain))
    g.write("--- IP START ---")
    g.write("\n")
    g.write(out)
    g.write("\t")
    apisite='http://ip-api.com/json/'+out
    daa=requests.get(apisite)
    dat=json.loads(daa.text)
    g.write("\t")
    g.write(dat['isp'])
    g.write("\t")
    g.write(dat['org'])
    g.write("\n")
    g.write("--- IP END START ---")
    g.write("\n\n")
    g.write("--- HEADERS START ---")
    g.write("\n")
    dom=str("https://www."+domain)   
    r = requests.get(dom)
    g.write(str(r.headers))
    g.write("\n")
    g.write("--- HEADERS END ---")
    g.write("\n\n")
    g.close()    
    with open("sitedetails.txt", "a", encoding="utf-8") as f:
        f.write("--- SOURCE START ---")
        f.write("\n")
        f.write(r.text)
        f.write("\n")
        f.write("--- SOURCE END ---")
