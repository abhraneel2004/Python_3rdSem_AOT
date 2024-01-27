
def cases(st):
    u = 0
    l = 0
    for i in st:
        if i.isupper():
            u+=1
        if i.islower():
            l+=1

    return u,l

s = input("Enter a string: ")
up, lo = cases(s)
print("No. of Uppercase characters: ", up)
print("No. of Lowercase characters: ", lo)