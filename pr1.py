def CtoF(c):
    return c * 9/5 + 32
def FtoC(f):
    return (f - 32) * 5/9
def CtoK(c):
    return c + 273.15
def KtoC(k):
    return k - 273.15

while True:
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    try:
        choice = int(input("choose conversion (1-4): "))
        if choice in range(1, 5):
         break
        else:
         print("incorrect , enter a number between 1 and 4")
    except ValueError:
        print("invalid, enter a numeric value")

while True:
    try:
        tmp = float(input("enter temperature: "))
        break
    except ValueError:
        print("invalid temperature ,enter a numeric value")


if choice==1:
    result = CtoF(tmp)
    print(tmp, "°C =", result, "°F")
elif choice ==2:
    result = FtoC(tmp)
    print(tmp, "°F =", result, "°C")
elif choice==3:
    result = CtoK(tmp)
    print(tmp, "°C =", result, "K")
elif choice ==4:
    result = KtoC(tmp)
    print(tmp, "K =", result, "°C")