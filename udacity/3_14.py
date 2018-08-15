age = {
    "Bao Ngoc": 15,
    "Ngoc Mai": 12,
    "Kim Lien": 48,
    "Van Chuong": 63
}

for key in age:
    print(key)

for key, value in age.items():
    print("Name: {}     Age: {}".format(key, value))