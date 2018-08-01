points = int(input())

if(points <= 50):
    result = "Congratulations! You won a wooden rabbit!"
elif(50 < points <= 150):
    result = "Oh dear, no prize this time."
elif(150 < points <= 180):
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"
print(result)