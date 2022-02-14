#file ko read vs code ki .py file karne ke lie
f=open("chirag.txt","rt")  #r defualt mode 
#content=f.read()  
#print(content)
#f.close()

#  line by line print karni hoto

#for line in f:
   # print(line,end="")
#f.close()

#ek line print karni ho tab readline ka use kare
#print(f.readline())

#line ko e list me print karne ke lie
print(f.readlines())
f.close()
