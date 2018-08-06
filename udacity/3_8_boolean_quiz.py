points = 174  #use this as input for your submission
prixe = None

if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points > 180:
    prize = "penguin"
    
if prize:
    result = ("Congratulations! You won a {}!".format(prize))
else:
    result = ("Oh dear, no prize this time.")


print(result)