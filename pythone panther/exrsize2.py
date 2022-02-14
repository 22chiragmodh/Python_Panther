#faulty calculator
print("enter first num")
a=int(input())
print("enter secon num")
b=int(input())
print("enter you want operation perform")
ope=input()
if(a==45 and b==3 and ope=='*'):
    print("555")
elif(a==56 and b==9 and ope=='+'):
    print("77")
elif(a==56 and b==6 and ope=='/'):
    print("4")
elif ope=='+':
      d=a+b
      print(d)
elif(ope=='*'):
      e=a*b
      print(e)
elif(ope=='/'):
      f=a/b
      print(f)
elif(ope=='-'):
      g=a-b
      print(g)
else:
    print("out of range")
