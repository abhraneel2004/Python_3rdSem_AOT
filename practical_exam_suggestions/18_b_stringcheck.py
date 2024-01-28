
def check(st):
    c=0
    for i in st:
        if i.isalpha():
            c+=1
            break
    for i in st:
        if i.isdigit():
            c+=1
            break
    return c==2

s = input("Enter the string: ")
print(check(s))