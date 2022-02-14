


list1=["2","4","6","8"]
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
list1[1]=list1[1]+3  
print(list1)  

sqr=list(map(lambda x:x,list1))
print(sqr)