
def avg_nums(str):
    if str[-1]=='q':
        str2 = str[:-2:]
        l = str2.split(' ')
        l = [int(i) for i in l]
        print(sum(l)/len(l))
        return
    print(str)
    return

s = input("Enter the string: ")
avg_nums(s)


'''

input: 1 2 3
str2 = "1 2 3"  
l = ['1','2','3']
l = []

'''

