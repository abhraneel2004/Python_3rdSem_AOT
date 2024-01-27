

def last_substring_index(str1, sbstr):
    str1, sbstr = str1.lower(), sbstr.lower()
    return str1.rfind(sbstr)

st = input("Enter the string:   ")
sb = input("Enter the substring: ")
idx = last_substring_index(st, sb)
if(idx==-1):
    print(f"The substring: {sb} not found in the string")
else:
    print(f"The last index of the substring: {sb} is {idx}")