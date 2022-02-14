from abc import ABC, abstractclassmethod, abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type="rectangle"
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def printarea(self):
        print("Area:")
        return self.length*self.width  
r1=rectangle(3,4)
print(r1.printarea())