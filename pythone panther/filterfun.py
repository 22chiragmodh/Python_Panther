list1=[1,2,3,4,5,6,8]
def isgreter(num):
    return num>5
# print(isgreter(3)) 

gt=list(filter(isgreter,list1))
print(gt)   



