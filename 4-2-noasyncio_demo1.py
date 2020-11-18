import time

def job(t):
    print('Start job',t)
    time.sleep(t)
    print('Job',t,'takes',t,'s')

if __name__=='__main__':
    t1=time.time()
    [job(t) for t in range(1,3)]
    print('No async total time:',time.time()-t1)