n=1
x=0
y=0
count=1
while count<n+1:
    if count%2 != 0:
        x+=10
        y=y
        count+=1
    else:
        y+=10
        x=x
        count+=1

a=str(x)+str(y)
print(a.split(","))
       
