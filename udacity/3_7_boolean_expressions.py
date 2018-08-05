weight = 55
height = 164

if 18.5 <= weight / height ** 2 < 25:
    print("Your BMI is considered normal.")
elif weight / height ** 2 >= 25:
    print("Your BMI is unnormal.")