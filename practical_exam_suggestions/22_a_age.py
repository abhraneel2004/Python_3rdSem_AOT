
age = int(input("Enter the age: "))
print("Age".center(10), "Status".center(10), sep = "|")
print("---------------------")

if age<2:
    print("<2".center(10), "in born".center(10), sep = "|")
elif age>=2 and age<=10:
    print("2-10".center(10), "child".center(10), sep = "|")
elif age>=11 and age<=17:
    print("11-17".center(10), "young".center(10), sep = "|")
elif age>=18 and age<=49:
    print("18-49".center(10), "adult".center(10), sep = "|")
elif age>=50 and age<=79:
    print("50-79".center(10), "old".center(10), sep = "|")
elif age>79:
    print(">80".center(10), "Very Old".center(10), sep = "|")
else:
    print("Invalid Age".center(21))