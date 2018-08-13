def read_input():
    n = int(input())

    apples, oranges = [], []
    for _ in range(n):
        apple_i, orange_i = tuple(map(int, input().split()))
        apples.append(apple_i)
        oranges.append(orange_i)

    return apples, oranges

def process(apples, oranges):
    n = len(apples)

    max_apple = -1
    count_max_apple = 0
    position_apple = -1
    for i in range(n):
        if apples[i] > max_apple:
            count = 1
            max_apple = apples[i]
            position_apple = i
        elif apples[i] == max_apple:
            count += 1

    if count_max_apple == 1:
        return position_apple

    max_orange = -1
    final_position = -1
    for i in range(n):
        if apples[i] == max_apple: 
            if oranges[i] > max_orange:
                max_orange = oranges[i]
                final_position = i

    return final_position

print(process(read_input()) + 1)
