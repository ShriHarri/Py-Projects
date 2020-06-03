num=525
c=0
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            c+=1
            break
        else:
            pass
       
print(c)
if c>0:
    print("composite")
else:
    print("prime")
