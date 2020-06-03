h="Hey mr ram"
t=h.split(" ")
k=[]
for i in t:
    f=""
    a= []
    u=i.split(" ")
    
    for e in u:
        
        for n in range (len(e)):
            if n>0:
                f+=e[n]
        f=f+e[0]+"ay"
        a.append(f)
        
        k.append(a)
q=""
for z in k:
    j=" ".join(z)
    q+=j
print(q)    
