num = int(input("Enter the number to find its factorial: "))
fact = 1
while num >= 1:
    fact *= num
    num -= 1 

print(f"The factorial is {fact}")