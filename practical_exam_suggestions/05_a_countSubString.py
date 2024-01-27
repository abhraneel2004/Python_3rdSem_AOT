
def countSubstring(str1, sbstr):
    str1, sbstr = str1.lower(), sbstr.lower()
    return str1.count(sbstr)

s1 = input("Enter a string: ")
s2 = input("Enter a substring: ") #input: India
print(countSubstring(s1, s2))
