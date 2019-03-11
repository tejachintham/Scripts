from threading import Thread
import requests
import Queue

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status = getStatus(url)
        print(status)
        q.task_done()

def getStatus(ourl):
    try:
        r = requests.get(ourl)
        datas=r.text
        return datas
    except:
        return "error", ourl

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in open('urllist.txt'):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
