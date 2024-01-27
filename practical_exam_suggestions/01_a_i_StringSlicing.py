
def shortString(st):
    if len(st)>2:
        return st[1:-1:1] 
    return st

print("After shortening: ",shortString(input("Enter a string: ")))