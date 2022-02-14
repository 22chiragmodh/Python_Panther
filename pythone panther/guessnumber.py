n=58
noofguess=1
while(noofguess<=9):
       print("Enter the user number and guess")
       gunum=int(input())
       if(gunum<n):
         print("Too low")
       elif(gunum>n):
         print("Too high....")
       else:
        print("you are Win!")
        print(noofguess,"no of guess he took to finish")
        break
       print(noofguess,"no of guess he took to finish")
       print(9-noofguess,"no of guess left")
       noofguess=noofguess+1

if(noofguess>9):
    print("Game Over")      


