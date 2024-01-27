
def num_to_word(num):
    l = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    if num >=0 and num<=9:
        return l[num]
    return "Invalid number"

n = int(input("Enter a number (0-9): "))
print(f"{n} in words is: {num_to_word(n)}")