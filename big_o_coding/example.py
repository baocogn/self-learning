import random

a = [random.randint(1, 100) for _ in range(10**4)]
n = 50

set_a = set(a)
for x in a:        # O(n)
    if n - x in set_a: # O(n)
        pass
