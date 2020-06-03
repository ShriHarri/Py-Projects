print("hi")

def guess(phrase):
    count=0
    for i in phrase:
        
        
        for j in ["a","e","i","o","u"]:
            
            if i==j :
                count+=1
          
    return count          


print(guess("aeiou"))        
