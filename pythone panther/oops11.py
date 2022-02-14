class A:
    var1="i am clas a var"
    def __init__(self):
        print("super class constructer")
    def greet(self,name):
        print("hello welcome"+name)
        
class B(A):
    var1="i am class b var"
    def __init__(self):
        super().__init__() #super se base class ka constucter bhi call hoga
        print("sub class constructer")
        self.var1="instant var b"
    def greet(self,name):  #override function
        print("good morning"+name)

b1=B()   #construceer override ho chuka hai 

print(b1.var1) #first instant variable dekhega super or sub badme varibale
b1.greet("chirag")  
