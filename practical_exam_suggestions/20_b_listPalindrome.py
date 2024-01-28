#void function
def palindrome(list_):
    for i in list_:
        if i==int(str(i)[::-1]):
            print(i, end = " ")
    
l = eval(input("Enter a list of numbers: "))
palindrome(l)
