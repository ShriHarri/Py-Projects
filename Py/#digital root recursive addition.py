
def ra (n):
    listr = []
    a=0
    while  n>0:
        a=n%10
        n=n//10
        listr.append(a)
        
    
    if sum(listr)>9:
        ra(sum(listr))
    else :
        print(sum(listr))





    
