def longest(s1,s2):
   
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in s1:
        l1.append(i)
    for i in l1 :
        if i not in l2:
            l2.append(i)
        

    
    
    for j in s2:
        l3.append(j)
    for j in l3:
        if j not in l4:
            l4.append(j)
        


    ans1=""
    ans2=""
    for f in l2:
        ans1+=f

    for g in l4:
        if g not in ans1:
            ans2+=g
    ans=ans1+ans2
    

    str="".join(sorted(ans))
    print(str)
    
longest("longest")
