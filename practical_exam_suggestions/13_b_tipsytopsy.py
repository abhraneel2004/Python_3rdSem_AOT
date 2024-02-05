
def tipsyTopsy(n):
    c3=1
    c7=3
    output=""
    for i in range(11,n+1):
        c3+=1
        c7+=1
        if c3==3:
            output+="Bhabi3"
            c3=0
        if c7==7:
            output+="Bhabi7"
            c7=0
        print(output or i)
        output=''

n = int(input("Enter a number N (N>20): "))
tipsyTopsy(n)