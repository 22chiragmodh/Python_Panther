f=open("harry.txt")
print(f.tell())
print(f.readline())
print(f.tell())  #character kis pointer par hai ye btata hai
print(f.readline())
print(f.tell())
f.close()