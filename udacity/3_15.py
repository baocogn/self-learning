# Quiz 1: FRUIT BASKET - task 1
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result
for fruit, amount in basket_items.items():
    if fruit in fruits:
        result += amount

print(result)

#Quiz 2: the same

#Quiz 3: FRUIT BASKET - task 3
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
#if the key is in the list of fruits, add to fruit_count.
#if the key is not in the list, then add to the not_fruit_count
for fruit, amount in basket_items.items():
    if fruit in fruits:
        fruit_count += amount
    else:
        not_fruit_count += amount

print(fruit_count, not_fruit_count)