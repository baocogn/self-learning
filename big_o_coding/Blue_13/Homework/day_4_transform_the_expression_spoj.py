t = int(input())
onb = list(map(input().split()))[:t]

# "(" occurs: skip it
# alphabets occur: print screen
# expressions: push into stack
# ")" occurs: output the expressions (one by one) in the stack


