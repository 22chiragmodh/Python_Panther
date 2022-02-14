class employee:
    nos=8
    def __init__(self,n,id,sl):
        self.name=n
        self.id=id
        self.salary=sl

    @classmethod
    def changenos(cls,nos1):  # nos variable ko koi bhi change kar sakta hai object or class dono
        cls.nos=nos1


harry=employee("harry","1234@3",18500)  
print(harry.id) 
print(harry.name);
print(harry.nos)
employee.nos=9  #class variable change karna classse hi hoga
print(harry.nos)
harry.changenos(67)   #class ka varible object se classmethod banake hi change hoga
print(harry.nos)    