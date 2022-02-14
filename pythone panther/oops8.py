#multiple inheritance   ->>
class A:
    def __init__(self):
        self.name1="tony stark"
        
    def display(self):
        print("class A method")

class B:
    def __init__(self):
        self.name2="steav rogers"
      
    def display2(self):
        print("class B method")  

class C(A,B):
    def display3(self,nm,id):
        print(nm+" "+id)

c1=C()  
print(c1.name1)

nm=input()  
id=input()
c1.display3(nm,id) 

                    