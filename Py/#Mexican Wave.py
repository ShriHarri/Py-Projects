s="hello world"
new=[]

for i in range(len(s)):
    if s[i] != " ":
        cap=s[i].upper()
    
        f="".join(s[:i]+cap+s[i+1 :])
        new.append(f)
    else:
        pass
            
print(new)
