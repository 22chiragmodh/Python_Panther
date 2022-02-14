class Animal:
    def __init__(self,aname,anum):
        self.name=aname
        self.num=anum

    @classmethod
    def fromstr(cls,string):
        # plist=string.split("-")
        # return cls(plist[0],plist[1])
        return cls(*string.split("-"))

         
wild=Animal("wild animal",34)
print(wild.name)  

soft=Animal.fromstr("soft animal-55")
print(soft.name)
