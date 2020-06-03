

def guess(phrase):
    count=0
    trans=""
    for i in phrase:
        
        
        if i in "aeiou":
            
          
                count+=1
                trans= trans + "0"
               
          
        else :
                trans = trans + i
          
    print (trans)
    return count          


print(guess("shri"))        
