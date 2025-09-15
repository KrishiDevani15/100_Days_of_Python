n = 5
sum = 0
for i in range(1,n+1):
    sum += i

print(f"th sum {n} is: {sum}")


# with formula (sum = n*(n + 1)/2) to reduce time complexity to O(1)
# n = int(input("Enter a number: "))
# sum = n * (n+1)//2
# print(sum)