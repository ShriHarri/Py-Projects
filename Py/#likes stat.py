l=["df","fg","fd","vf"]
if len(l) == 0:
    print("no one likes this")
elif len(l)== 1 :
    print(l[0] + " likes this")
elif len(l)== 2 :
    print(l[0] +" and " + l[1] + " like this")
elif len(l)== 3 :
    print(l[0] + "," + l[1] + " and " + l[2] + " like this")
elif len(l)> 4 :
    print(l[0] +" , "+ l[1] + " and " + str(len(l)-2)+ " others like this")
