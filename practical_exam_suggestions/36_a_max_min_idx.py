def max_min_idx(l):
    return [max(l),l.index(max(l)), min(l), l.index(min(l))]

l = eval(input("Enter the list: "))
m = max_min_idx(l)
print(f"Maximum Value: {m[0]}")
print(f"Maximum Index: {m[1]}")
print(f"Minimum Value: {m[2]}")
print(f"Minimum Index: {m[3]}")