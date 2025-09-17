staff = [("Amit",16),("Zara",17),("Raj",15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")

# Note in while-else and for-else, the else block is executed only when the loop is not terminated by a break statement.