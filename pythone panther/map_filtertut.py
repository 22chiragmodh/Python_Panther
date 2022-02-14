num=["2","3","5","8"]
# for i in range(len(num)):
#     num[i]=int(num[i])
# num[1]=num[1]+9
# print(num)    

# using map
# num=list(map(int,num))  #all string number int me convert hoge
# num[2]=num[2]+7
# print(num)


# map function se bhi ye kam kar sakte hai
number=[1,2,3,4,5,6,7,8,9]
sq=list(map(lambda x:x*x,number))
print(sq)  