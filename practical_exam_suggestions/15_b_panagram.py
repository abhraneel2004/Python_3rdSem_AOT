
def panagram(st):
    st = st.lower()
    alpha = [chr(97+i) for i in range(26)]
    for i in alpha:
        if i not in st:
            print(i, "is not in the string")
            return False
    return True

# s = "The quick brown fox jumps over the lazy dog"
s = input("Enter a string: ")
if (panagram(s)):
    print("The given string is a Panagram")
else:
    print("The given string is NOT a Panagram")