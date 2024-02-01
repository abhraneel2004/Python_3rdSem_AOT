
def uglyNum(n):
    if not n%2 or not n%3 or not n%5:
        return True
    return False

a = int(input("Enter a number: "))
if(uglyNum(a)):
    print("The Number is Ugly")
else:
    print("The Number is NOT Ugly")