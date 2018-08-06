n = int(input())



def process(n):
    count = 0   
    for ans in n:
        for i in range(len(n)):
            if ans[i] == 1 and ans[i] == ans[i+1]:
                count += 1
            elif ans[i] == 0 and ans[i] == ans[i+1]:
                count += 0
    return count

print(process(n)

    


        
    