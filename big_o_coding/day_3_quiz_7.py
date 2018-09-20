n = int(input())

a = [
    [" " for _ in range(n)] for _ in range(n)
]
 
for i in range(n):
    a[i][0]   = "*"  # left-most column
    a[0][i]   = "*"  # top row
    a[i][n-1] = "*"  # right-most column
    a[n-1][i] = "*"  # bottom row

for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print()

for i in range(0, n):
    for j in range(0, n):
        if i == j: # This indicates the main diagonal
            print("*", end="")  
        elif i + j == n - 1: # This indicates the extra diagonal
            print("*", end="")  
        # This indicates the top row
        elif i == 0:          
            # Usually the print() function will print the content with a new line.
            # In order to do this problem, we need the `end` argument of the print() function.
            # Basically, print("#", end="") means we just print out the single character '*'
            # without entering a new line.
            print("*", end="")  
        # This indicates the left-most column
        elif j == 0:        
            print("*", end="")
        # This indicates the lowest row
        elif i == n - 1:
            print("*", end="")
        # This indicates the right-most column
        elif j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # This will print a new line
