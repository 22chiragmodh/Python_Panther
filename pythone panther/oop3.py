class School:
    nos=34
    def __init__(self,name,salary,id): 
        self.name=name
        self.salary=salary
        self.id=id
name=input()
salary=input()
id=input()
obj=School(name,salary,id)
print(obj.name)        
print(obj.salary)        
print(obj.id)        
    # def printdetails(self):
    #     return f"name is {self.name} marks is {self.marks}"

# mahi=School()
# jagat=School()
# mahi.name="m.s.dhoni"
# mahi.marks="95/100"
# jagat.name="johson"
# jagat.marks="92/100"
# print(mahi.printdetails())    #mahi.fun karne par mahi self ban jayega or return vali f strig print hogi mahi ke lie
# print(jagat.printdetails())    