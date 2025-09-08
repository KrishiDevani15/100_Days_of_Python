
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

if (num1 > num2) and (num1 > num3):
    print(f"{num1} is Greatest")
elif (num2>num3):
    print(f"{num2} is Greatest")
else:
    print(f"{num3} is Greatest")