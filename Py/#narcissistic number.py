n=153
x=[]
y=[]
while n>0:
    a=n%10
    n=n//10
    x.append(a)
for i in x:
    p= i**len(x)
    y.append(p)
print(y)    
sumis=0
for i in y:
    sumis+=i
print(sumis)    
