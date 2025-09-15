'''
Count Digit of a Number
Logic
    1) start counting from backside --> n // 10 (to remove last number)
    2) Then increment counter

'''

n = int(input("Enter Number: "))
counter = 0
while n > 0:
    counter += 1
    n = n // 10

print(f"Number of Digits: {counter}")