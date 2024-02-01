
l = eval(input("Enter the list: "))
l = [int(i) for i in l]
mean = sum(l)/len(l)

l2 = [(k-mean)**2 for k in l]
var = sum(l2)/len(l)
print("Arithmetic Mean: ",mean)
print("Variance : ",var)
print("Standard Deviation: ",var**0.5)
