print("What's the weather like?")
weather = str(input())

if weather == "snow":
    print("Wear your coat!")
elif weather == "rain":
    print("Take your umbrella with you!")
elif weather == "sun" or weather == "wet":
    print("Bring a bottle of water with you!")

ans = str(input())
if ans == "Ok":
    print("Love you, have a good day!")
elif ans == "No I won't":
    print("That's bad of you!")
elif ans == "Thanks mom":
    print("Uhm that's kind of you!")

