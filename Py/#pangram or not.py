s="asdfg"
a=[]
count=0
for i in range(len(s)):
    a.append(s[i])

for j in a:
    if j in "abcdefghijklmnopqrstuvwxyz" :
        count+=1
    else :
        pass


if count == 26:
    print("pangram")
else :
    print("not")
