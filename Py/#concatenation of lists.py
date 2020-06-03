l=[1,2,3,4,5,6,[],9,"a",0,0,"b"]
z=[]
nz=[]
for i in l:
    if i == 0:
        z.append(i)
        print(z)
    else :
        nz.append(i)
        print(nz)

ans= nz+z
print(ans)
