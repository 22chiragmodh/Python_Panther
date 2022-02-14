def split_join(str):
    str=str.split(" ")  #split me " "se string me space ayegi vahase alag alag string ki list banegi
    str1="-".join(str) 
    return str1 
str=input()    
result=split_join(str)
print(result)    