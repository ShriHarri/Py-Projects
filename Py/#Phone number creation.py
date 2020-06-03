s1="cedewaraaossoqqyt"
s2="codewars"
l1=[]
l2=[]
new=[]
for i in range(len(s1)):
    l1.append(s1[i])

for j in range(len(s2)):
    l2.append(s2[j])
l2.sort()

for l in l1:
    if l in l2:
        
        new.append(l)
    else:
        pass
new.sort()

print(l2)
print(new)



