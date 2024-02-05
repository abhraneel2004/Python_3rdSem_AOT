
def d_2_bo(n,b):
    s=''
    temp = n
    while(temp>0):
        r = temp%b
        s+=str(r)
        temp = temp//b
    s = s[::-1]
    return s

def d_2_h(n):
    l=['A','B','C','D','E','F']
    s=''
    temp = n
    while(temp>0):
        r = temp%16
        if (r>9):
            s+=l[r-10]
        else:
            s+=str(r)
        temp = temp//16
    s = s[::-1]
    return s

num = int(input("Enter the decimal number: "))
base = int(input("Enter the base (2/8/16): "))
if base==2:
    print(d_2_bo(num, base))
elif base==8:
    print(d_2_bo(num,base))
elif base==16:
    print(d_2_h(num))
else:
    print("Invalid base")