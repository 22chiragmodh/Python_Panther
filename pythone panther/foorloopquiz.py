list1=[2,6,8,9,3,1,10]
# list me se 6 se bade number hi print arne hai
for item in list1:
    if(item>6):
        print(item)

#  list ma string and number dono ek sath ho to str(item).isnumeric() and item<6 likhna padega 
l2=["hy",86,3,4,92,1,5,"by"]
for item in l2:
    if(str(item).isnumeric() and item>6):
        print(item)
