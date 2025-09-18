# Factorial is product of n natural number same as sum of n natural number instead of + --> *
num = int(input("Enter a number to find its factorial: "))
factorial  = 1
for i in range(1,num+1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")