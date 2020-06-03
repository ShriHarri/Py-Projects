s="how are you"
sp=s.split()
print(sp)
new=[]
for i in sp:
    i=i.capitalize()
    new.append(i)
jo=" ".join(new)
print(jo)
print(sorted(jo))
print(sorted(s))
