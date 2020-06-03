n=4532

asd=[]
while n>0:
    a=n%10
    n=n//10
    asd.append(a)
    


qwe=[]
for i in asd :
    b= i**2
    qwe.append(b)
    
qwe.reverse()

c=""
for i in qwe:
    c+=str(i)
    
print(c)



    
