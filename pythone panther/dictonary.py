d1={"chirag":"vagitable","nilam":"non vegitable","chaki":"idlidhosha"}
print(d1)
# nilam kya khati hai ye print dictonary se karvaya
print(d1["nilam"])
# ek dictonary kr andar bhi dictonary rakh sakte hai
d2={"shubham":"chikan","mehul":"roti","anubhav":"burger","saurabh":{"B":"meggi","L":"dal-chaval","D":"biryani"}}
print(d2["saurabh"])
# dictonary me add bhi kar sakte hai
d2["rahul"]="junk food"
d2["auragzeb"]="kabab"
print(d2)
# remove bhi kar sakte hai dictonary me se
del d2["saurabh"]
print(d2)
print(d2.keys())
print(d2.items())