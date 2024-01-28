
def isbinary(st):
    for i in st:
        if i not in ("0","1"):
            return "No"
    return "Yes"

s = input("Enter a string: ")
print(isbinary(s))