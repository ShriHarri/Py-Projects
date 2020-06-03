r=10
sume=0
for i in range(r):
    
    if i%3 == 0 or i % 5 == 0:
        print("yes" + str(i))
        sume+=i
        print(sume)
