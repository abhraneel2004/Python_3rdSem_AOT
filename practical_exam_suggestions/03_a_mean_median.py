

def meanList(l):
    return sum(l)/len(l)

def medianList(l):
    l.sort()
    return l[len(l)//2]

lt = eval(input("Enter a list of integers:  "))
print("Mean: ",meanList(lt))
print("Median: ",medianList(lt))