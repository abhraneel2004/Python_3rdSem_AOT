a = (11, [22, 33], 44, 55)
a = list(a)
a[1][0] = 222
a = tuple(a)
print(a)
