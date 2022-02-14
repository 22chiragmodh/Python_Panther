import time
intial=time.time()  #intial time second.milisecond me deta hai

k=0
while(k<30):
    print("chirag & anubhav")
    time.sleep(2)  #2 secondruk ke print karega
    k=k+1
print("time run while loop:",time.time()-intial)
intial2=time.time()
for i in range(30):
    print("chirag & anubhav")
print("time run for loop:", time.time()-intial2)