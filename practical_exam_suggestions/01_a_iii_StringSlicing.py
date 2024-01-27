
def newString2(str1, str2):
    return str1[0:len(str1)//2:1]+str2+str1[len(str1)//2::]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(newString2(s1, s2))