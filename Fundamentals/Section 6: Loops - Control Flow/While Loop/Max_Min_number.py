num = int(input("How many numbers will you enter? "))

max_num = None
min_num = None

counter = 0
while counter < num:
    X = int(input(f"Enter number {counter + 1}: "))
    
    if max_num is None or X > max_num:
        max_num = X

    if min_num is None or X < min_num:
        min_num = X

    counter += 1

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
