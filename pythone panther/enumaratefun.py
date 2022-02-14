l1=["allo-matar","onion","pizaa","burger","manchuriyan","sole-bhature","idali-dhosha","chauman","sandwitch","bradpakoda"]
# for item in l1:{
#    print(item,end=" ")
# }
# muje bas even ya odd vale print karane ho tab ek ek print karne se enumarate fun ka use kare
for i,item in enumerate(l1):
    if i%2==0: 
        print(f"even sabji print:{item}")