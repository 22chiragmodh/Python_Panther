

#client_name = ["Harry", "Chirag", "Anubhav"]
#log_list = ["Exercise", "Diet"]


client_list={1:"Harry",2:"Chirag",3:"Anubhav"}
log_dic={1:"Exercise",2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

print("## HEALTH MANAGMENT SYSTEM WITH PYHTON ##\n")

print("Select client name:","\n")
for key,name in client_list.items():
    print("press",key,"for",name,"\n")
client_name=int(input("\n"))
print(client_list[client_name],"selected","\n")

print("press 1 for Exercise"," || ","press 2 for Diet\n")
log_name=int(input())
print(log_dic[log_name],"selected","\n")
if(log_name==1):
    
    f = open(client_list[client_name] + log_dic[log_name] + ".txt", "a")
    k='y'
    while(k!='n'):
     print("Enter exercise Type:")
     ex_name= input()
     f.write('date and time - [' + str(getdate()) + '] : '+"Exercise name-" + ex_name + '\n')
     k=input("ADD MORE?y/n:")
     continue
     f.close()
if(log_name==2):
    f_1 = open(client_list[client_name] + log_dic[log_name] + ".txt", "a")
    k='y'
    while(k!='n'):
     print("Enter Diet Type:")
     di_name= input()
     f_1.write('date and time - [' + str(getdate()) + '] : '+"Diet name-"+ di_name + '\n')
     k=input("ADD MORE?y/n:")
     continue
     f_1.close()
    







