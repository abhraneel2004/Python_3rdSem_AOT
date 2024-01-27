
def avg_nums(str):
    q = str[-1]
    if q=='q':
        str2 = str[:-2:]
        l = str2.split(' ')
        l = [int(i) for i in l]
        print(sum(l)/len(l))
        return
    print(str)
    return

s = input("Enter the string: ")
avg_nums(s)