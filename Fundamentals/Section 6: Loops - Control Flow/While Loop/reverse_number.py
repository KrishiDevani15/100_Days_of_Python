num = int(input("Enter a number: "))
print(f"You entered {num}")
reverse_num = 0
is_negative = num < 0

if is_negative:
    num = -num  # Work with positive version of number

while num > 0 :
    rem = num % 10
    reverse_num = (reverse_num * 10) + rem
    num //= 10

if is_negative:
    reverse_num = -reverse_num # again making it negative
print(f"The reverse number is: {reverse_num}" )