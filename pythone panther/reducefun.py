from functools import reduce
list=[2,4,6,8,10]
# sum=0
# for item in list:
#     sum=sum+item
# print(sum)    

sum=reduce(lambda x,y:x*y,list)    
print(sum)