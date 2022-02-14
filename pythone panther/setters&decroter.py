class Employee:
    def __init__(self,nm1,nm2):
        self.name1=nm1
        self.name2=nm2
        #self.email=f"{self.name1}.{self.name2}@gmail.com"
    def explain(self):
        return f"this employee is {self.name1} and {self.name2}"

    def email(self):
        return f"{self.name1}.{self.name2}@gmail.com"
h1=Employee("harry","chirag")
print(h1.explain()) 
p1=Employee("maqbool","amirhusen")  
print(p1.explain())     
h1.name2="anubhav" 
#print(h1.email)                     #direct h1.name="name" karke print(h1.email) kaenge to chirag ki  jagah anubhav nhi ayega run
print(h1.email()) 
                     #runtime me constructer me chirag diya hai argument me isliye function me likhke run krna