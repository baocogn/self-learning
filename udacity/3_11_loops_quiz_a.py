# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []

# # write your for loop here
# for name in names:
#     username = name.lower().replace(" ", "_")
#     usernames.append(username)

# print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")
    
print(usernames)