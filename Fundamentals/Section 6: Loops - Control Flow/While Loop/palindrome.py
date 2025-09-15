num = int(input("Enter a number:"))
original_num = num
reverse_num = 0
is_negative = num < 0

if is_negative:
    num = -num

while num > 0:
    r = num % 10
    reverse_num = (reverse_num * 10) + r
    num = num // 10

if is_negative:
    reverse_num = -reverse_num

if original_num == reverse_num:
    print(f"{original_num} is a palindrome")
else:
    print(f"{original_num} is not a palindrome")    