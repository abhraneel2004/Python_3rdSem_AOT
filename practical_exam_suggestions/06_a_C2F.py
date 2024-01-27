
def centigrade_to_fahrenheit(c):
    n = (9/5)*c+32
    return n

def fahrenheit_to_centigrade(f):
    n = (f-32)*(5/9)
    return n

c1 = int(input("Enter temperature in Centigrade: "))
print("Temperature in Fahrenheit: ", centigrade_to_fahrenheit(c1))

f1 = int(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius: ", fahrenheit_to_centigrade(f1))