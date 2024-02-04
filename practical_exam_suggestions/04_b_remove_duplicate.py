
def removeDup(str1):
    l = [k for k in str1]
    m = []
    for i in l:
        if i not in m:
            m.append(i)
    # print(m)
    '''
        "-".join(['a', 'b', 'c', 'd', 'e', 'f]) = "a-b-c-d-e-f"

        "%".join(['a', 'b', 'c', 'd', 'e','f']) = "a%b%c%d%e%f"
        
    '''
    return "".join(list(m))

print(removeDup(input("Enter the string: ")))