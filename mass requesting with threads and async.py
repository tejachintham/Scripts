from threading import Thread
import grequests
import Queue
concurrent = 20

def doWork():
    while True:
        url = q.get()
        status = getStatus(url)
        print(status)
        q.task_done()

def getStatus(ourl):
    try:
        rs = (grequests.get(us) for us in ourl)
        requests = grequests.map(rs)
        for response in requests:
            try:
                g=open(lis[v].strip()+".txt","w+")
                g.write(response.content)
                v=v+1
            except:
                g=open("fails.txt","a+")
                g.write(lis[v].strip())
                v=v+1        
    except:
        return "error", ourl

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    f=open("urllist.txt")
    urls=f.readlines()
    urllis=[]
    lis=[]
    v=0
    ld=[]
    for u in urls:
        u=u.strip()
        y=u.split(",")
        lis.append(y[1])
        u="http://"+y[1]
        urllis.append(u)
    for u in urllis:
        ld.append(u)
        if(len(ld)>400):
            longlis.append(ld)   
            q.put(ld)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
