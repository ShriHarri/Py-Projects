d="2 4 5 6 8"
e= d.split(" ")
ev=[]
od=[]
a=[]
for i in e:
    
    j=int(i)
    a.append(j)

for i in a :
    if i%2 == 0:
        ev.append(i)
    else :
        od.append(i)

if len(ev)== 1:
    
    ind=a.index(ev[0])
    indexof=ind+1
    print(indexof)
else:
    print(od)
    ind=a.index(od[0])
    indexof=ind+1
    print(indexof)
