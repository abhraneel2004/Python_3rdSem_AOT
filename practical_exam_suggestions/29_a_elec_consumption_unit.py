
a = int(input("Enter the Electricity consumption amount in Units: "))
if a>=0 and a<=200:
    price = a/2
    print(f"Amount to be payed in Rs = {price}")
elif a>200 and a<401:
    price = 100 + (0.65*(a-200))
    print(f"Amount to be payed in Rs = {price}")
elif a>400 and a<601:
    price = 250 + (0.8*(a-400))
    print(f"Amount to be payed in Rs = {price}")
elif a>600:
    price = 450 + (1.25*(a-600))
    print(f"Amount to be payed in Rs = {price}")
else:
    print("Invalid consumption amount given.")