# num=[2,4,6,8,10]
def square(n1):
     return n1*n1

def cube(n1):
     return n1*n1*n1
func=[square,cube]
for i in range(10):
    val=list(map(lambda x:x(i),func))
    print(val)
    