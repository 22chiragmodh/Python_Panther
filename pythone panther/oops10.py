class base:
    var1=8
    _var2=45
    __var3=67
    def display(self):
        print(self.__var3)
   
class derrived(base):
    a=89
    b=6    

d1=derrived() 
print(d1.var1)   
print(d1._var2)   
d1.display()
