f=open("harry.txt")
print(f.readline())
f.seek(5)        #pointer ko reset arne ke lie 5 charcter se print hoga
print(f.readline())
print(f.readline())
f.seek(18)
print(f.readline())
f.close()