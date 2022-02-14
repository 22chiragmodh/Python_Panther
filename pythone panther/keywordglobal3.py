l=12
# l=12 global variabal hai usko kisi function me change karne ke lie global var likhna padta hai
def function1():
    
    global l
    l=l+58
    l=23
    print(l)
function1()
    #  jab function ko call larenge tab vo uska local var dekhega badme global dekhega
x=78
def harry():
    x=20
    def chik():
        global x
        x=50
    
    print("before calling chik x=",x)
    chik()
    print("after calling chik x=",x)
    # jab harry fun ko call karenge tab uske andar vala x=20 hi print hoga 
harry()
# function hrry ke bad x print karenge tab global x print hoga
print(x)  