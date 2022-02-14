def funargs(normal,*args):   #normal argument ko first rakhe
    print(normal)
    for item in args:
        print(item,end=" ")
      
    print(type(args))  #type args ki touple hoti hai
normal="i am normal student in school :"    
str=["harry","chirag","mukesh","anubhav","naresh"]    #str me jitne add karte jaenge utne print hote jaenge args se
funargs(normal,*str)
