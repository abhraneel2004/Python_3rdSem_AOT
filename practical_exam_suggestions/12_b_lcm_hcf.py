
def hcf(max_, min_):
    hcf_ = 1
    for i in range(1,min_+1):
        if max_%i==0 and min_%i==0:
            hcf_ = i
    return hcf_

def lcm(max_, min_):
    return (max_ * min_)/hcf(max_, min_)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print(f"LCM of {a} and {b} is:",lcm(a,b))
    print(f"HCF of {a} and {b} is:",hcf(a,b))
else:
    print(f"LCM of {a} and {b} is:",lcm(b,a))
    print(f"HCF of {a} and {b} is:",hcf(b,a))
