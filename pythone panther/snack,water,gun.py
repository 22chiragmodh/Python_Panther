import random
print("## *Hello Chirag you are playing Snake-Water-Gun game* ##")

print("your choice:")
un=int(input("0=Snake && 1=Water && 2=Gun\n"))
cn=random.randint(0,3)
if(cn==0):
    print("computer choise is:Snake")
elif(cn==1):
    print("computer choice is:water")    
else:
    print("computer choice is:Gun")    
if((un==0 and cn==1) or(un==1 and cn==2) or(un==2 and cn==0)):
    print("You are won game!!")
elif(cn==un):
    print("game draw")
else:
    print("computer won the game.")    

