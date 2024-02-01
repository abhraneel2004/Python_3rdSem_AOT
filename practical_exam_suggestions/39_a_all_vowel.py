

def all_vowel(st):
    l = ['a','e','i','o','u']
    st = st.lower()
    for i in st:
        if i in l:
            l.remove(i)
    return not len(l)

s = input("Enter the string: ")
if (all_vowel(s)):
    print("Accepted")

else:
    print("Rejected")