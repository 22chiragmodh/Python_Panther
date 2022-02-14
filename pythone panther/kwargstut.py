def funkwargs(normal,**kwargs):
    print(normal)
    for key,value in kwargs.items():
    #    print(key,"is a",value) or fstring se kar sakte hai
         print(f"{key} is a {value}")
normal="4 person and his job:"
dix={"harry":"programer","ganesh":"farmer","mahesh":"photographer","jayesh":"builder","shiv":"kock"}
funkwargs(normal,**dix)     