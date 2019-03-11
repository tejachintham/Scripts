import grequests
import gevent
urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)
requests = grequests.map(rs)
for response in requests:
    print(response)
