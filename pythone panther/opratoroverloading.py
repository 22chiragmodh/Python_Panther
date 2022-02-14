class emp:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
     
    def __add__(self,other):  #operator overloading dunder method
        return self.salary+other.salary

    def __truediv__(self,other):   #dunder method
        return int(self.salary/other.salary)  
e1=emp("hary",240000,"programer")       
 
e2=emp("chirag",12000,"coder")

print(e1/e2)  #dunder add ke bina object+object not valid