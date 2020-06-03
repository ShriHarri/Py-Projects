secret = "shri"
guess = ""
i=1
print("Welcome to Guessing game ")
while secret != guess and i <= 3:
    print(str(i) + " chance")
    guess = input("Enter a guess word : ")
    i+=1
    


if i >= 3 and secret!= guess :
    print("Out of chances")
elif i >= 3 or secret==guess :
    print("You win")
   



        
