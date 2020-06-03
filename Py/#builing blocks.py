m="l"
sume=0
if m > 0:
    for i in range(int(m/2)):
        if sume < m:
            sume+= i**3
        elif sume == m:
            print(i-1)
            break
        elif sume >  m :
            print("-1")
            break

else:
    print("-1")

