#cookie box  and container

x = int(input("Enter the no. of cookies: "))
box = x//24
l1 = x%24
container = box//75
l2 = box%75

print("No of boxes: ", x%24)
print("No of leftover cookies: ", x%24)
print("No of containers: ", container)
print("No of leftover boxes: ", l2)
