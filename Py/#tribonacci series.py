a=[3,2,0]
n= len(a)
req=1
new=[]
new1=[1]
if req == 1:
    print(new1)
elif req == 0:
    print(new)
else:
    while len(a)< req:
        s=a[-1]+ a[-2]+ a[-3]
        a.append(s)
    

print(a)
