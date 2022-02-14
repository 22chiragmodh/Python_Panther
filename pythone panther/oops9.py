#multilevel inheritance
class Dad:
    dance=1
         
    def display(self,age):
        
        print("dad age is",age)
        

    
class Son(Dad):
    dance=2
    def display2(self,age,name):
        print(name+" age is ",age)
        
class grandson(Son):
    dance=4
   
    def display3(self,name,age,bornplace):
        print(name+" born at "+bornplace+" his curent age is",age)

gs=grandson()
age=int(input())
name=input()
bornplace=input()
gs.display(age)
gs.display2(age,name)
gs.display3(name,age,bornplace)
print(gs.dance)