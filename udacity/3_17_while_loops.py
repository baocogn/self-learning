cards = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# while sum(hand) <= 17:
while sum(hand) <= 18:
    hand.append(cards.pop())

print(hand)