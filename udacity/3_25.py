# manifest = [("desks", 15),
# ("chairs", 60),
# ("blankets", 10),
# ("cabinets", 7)
# ]

# for x in manifest:
#     item, weight = tuple(x)


# items = ["bananas", "machine", "apples", "desks", "phones"]
# weights = [15, 34, 42, 120, 5]

# print(list(zip(items, weights)))

# for i, item in zip(range(len(items)), items):
#     print(i, item)

# for i, item in enumerate(items):
#     print(i, item)

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letters, nums))

some_list = (('a', 1), ('b', 2), ('c', 3))

A, N = zip(*some_list)
# print("{}: {}".format(A, N))
print(A)
print(N)

for i, letter in enumerate(letters):
    print(i, letter)