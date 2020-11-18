import time

import requests

URL='https://mofanpy.com/'

def normal():
    for i in range(2):
        r=requests.get(URL)
        url=r.url
        print(url)

t1=time.time()
normal()
print('Normal total time',time.time()-t1)