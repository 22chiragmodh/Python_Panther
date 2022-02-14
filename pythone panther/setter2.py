#setter ka use karke argument change kar sakte hai setter1 se jayada upyogi rahega 
class Employee:
    def __init__(self,nm1,nm2):
        self.name1=nm1
        self.name2=nm2
    
    @property
    def email(self):
        if self.name1==None or self.name2==None:
            return "email is not set..using setter"
        else:   
            return f"{self.name1}.{self.name2}@gmail.com"

    @email.setter   #name1 and name2 ko set karega
    def email(self,string):
        name=string.split("@")[0]  #@ se tutega string or @ke pahela vala store karega
        self.name1=name.split(".")[0]  #. ke pahele ka stor hoga
        self.name2=name.split(".")[1]

    @email.deleter  #name1 and name2 delete=none karne ke lie
    def email(self):
        self.name1=None
        self.name2=None  

h1=Employee("harry","chirag")
print(h1.email)
h1.email="this.that@gmail.com"
h1.name1="hindustani"  
h1.name2="supporter"
print(h1.email)
del h1.email
print(h1.email)

