# Fibsieve's Fantabulous Birthday
import math
 
T = int(input())
for tc in range(1, T + 1):
    print('Case %d:' % tc, end = ' ')
    S = int(input())
    n = math.ceil(S ** 0.5)
    x = y = n
    if n * n - S < n:
        y = n ** 2 - S + 1
    else:
        x = S - (n - 1) ** 2
    if n % 2 == 1:
        print(y, x)
    else:
    	print(x, y)
 