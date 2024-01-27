
def newString(str1, str2):
    return str1[0]+str1[len(str1)//2]+str1[-1]+str2[0]+str2[len(str2)//2]+str2[-1]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(newString(s1, s2))