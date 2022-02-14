a=3
b=8
c=9
d=12
e=45
f=89
print(sum((a,b,c,d,e,f))) #built in function

#user deine function
def function(a,b):
    print("sum=",a+b)
    print("diff=",a-b)
    print("mult=",a*b)
    print("divi=",a/b)
    print("rem=",a%b)
function(15,6) # none return function()

def average(c,d,e):
    """average function hai 3 number ki average nikalta hai"""
    avg=(c+d+e)/3
    return avg
#print(average(5,8,8))   #return type function ko pint ke nadar lihna padta hai
print(average.__doc__)  #docstring print karne ke lie