
def leapyear(year):
    if (year%4==0):
        if (year%100==0 and year%400!=0):
            return False
        return True
    return False

y = int(input("Enter the year: "))
if leapyear(y):
    print("The given year is a Leap Year")
else:
    print("The given year is not a Leap Year")
