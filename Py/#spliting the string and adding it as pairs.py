s="b"
a=[]
new=[]
for i in range(len(s)):
    a.append(s[i])
print(a)
if len(a)%2 == 0:
    for i in range(len(a)):
        if  i%2 != 0:
            print(i)
            f= s[i-1] + s[i]
            new.append(f)
        else:
            pass

else:
    for i in range(len(a)):
        print(s[i])
        if i < len(a) -1:
            if  i%2 != 0:
                print(i)
                f= s[i-1] + s[i]
                new.append(f)
            else:
                pass    

        else:
            p= s[len(a)-1] + "_"
            new.append(p)




print(new)
