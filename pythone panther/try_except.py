# jab program ke bich me error ho or uske age vala print karvana hai tab try except ka use karte hai
a=input() 
b=input()
try:
    print(int(a)+int(b)) #jab input a ya b me se koi string lege ya char tab error ayegi or age vala run nhi hoga
except Exception as e:
    print(e)
print("i am important line must be print")
#program ko eror se exit hone se bachata hai