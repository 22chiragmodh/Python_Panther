class programmer:
    nol=8
    def __init__(self,lname):
        print("\nprogramer use following website for coding:\n"+lname)
        
class coder(programmer):
    noluse=4
    
    def __init__(self, lname,sub):
        print(f"{lname} and topic are: {sub}")
    @staticmethod
    def printlng(nm,id,string):
        print(nm+" id is "+id+" is"+" use following lang:\n"+string)
harry=coder("Python",["string","oops","constructer","inheritance"])
harry.printlng("Harry","#harry123@","C->>C++->>Java->>Python")
print(harry.nol)