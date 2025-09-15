num = int(input("Total number of natural number to be added: "))
sum = 0
i = 0
while num > i:
    sum += int(input("Enter number: "))
    i += 1

print(f"Sum for {num} natural number is: {sum}")