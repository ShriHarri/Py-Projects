s="uncopyrightable"
a=[]
new=[]
count= 0
for i in range(len(s)):
    a.append(s[i])

for j in a:
    if j  not in new:
        
        new.append(j)

    else:
        pass

if len(a)== len(new):
    print("Isogram")
else:
    print("not")


    
