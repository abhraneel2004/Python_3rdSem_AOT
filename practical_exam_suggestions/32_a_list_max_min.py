
l = eval(input("Enter the list: "))
si = int(input("Enter the starting index: "))
ei = int(input("Enter the ending index: "))
if si>=0 and ei<len(l):
    print(f"Maximum from the given sublist {max(l[si:ei])}")
    print(f"Minimum from the given sublist {min(l[si:ei])}")