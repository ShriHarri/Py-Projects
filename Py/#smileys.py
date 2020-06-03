a=[":)", ";(", ";}", ":-D"]
new=[]
for i in a:
        
    if i[0] in ":;" :

        if len(i)==2:
            if i[1] in ")D":
                new.append(i)
            else :
                pass
        elif len(i)==3:
            if i[1] in "-~" and i[2] in ")D":
                new.append(i)
            else:
                pass

    else:
        pass


print(len(new))
