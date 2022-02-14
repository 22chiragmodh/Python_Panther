a=[5,3,7,2,8,1]
a.sort()
print(a)

b=[[2,5],[1,4],[6,3],[0,8]]
# b.sort()
print(b)
# index 1 ke anusar sort karna ho to lambda function ka use kar saktehai   [0,1]
b.sort(key=lambda x:x[1])
print(b)

