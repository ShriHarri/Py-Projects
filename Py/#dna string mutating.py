dna="attgc"

new=""
for i in dna:
    
    if i == "a":
        i= "t"
        new+=i
    elif i == "t":
        i="a"
        new+=i
    elif i == "g":
        i="c"
        new+=i
    elif i== "c":
        i="g"
        new+=i
print(new)        
