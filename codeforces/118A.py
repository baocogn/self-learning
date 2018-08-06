a = str(input())

def remove_vowels(a):
    a = a.replace('a', '')
    a = a.replace('e', '')
    a = a.replace('i', '')
    a = a.replace('o', '')
    a = a.replace('u', '')
    a = a.replace('y', '')

    return a

def insert_periods(a):
    string = []
    for char in a:
        string.append(".")
        string.append(char)
    
    return "".join(string)

def lower_case(a):
    return a.lower()

def process(a):
    a = lower_case(a)
    a = remove_vowels(a)
    a = insert_periods(a)
    
    return a

print(process(a))