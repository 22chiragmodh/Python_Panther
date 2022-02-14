class A:
    def greet(self):
        print("method class A")

class B(A):
    def greet(self):
        print("method class B")
        

class C(A):
    def greet(self):
      print("method class c")


class D(B,C):  # B C me jo first (b,c)hoga uska function run hoga ambimguity
    def greet1(self):
        print("method class D")        

d1=D()   
d1.greet()   
d1.greet1()   