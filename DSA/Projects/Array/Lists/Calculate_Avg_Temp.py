numbers_of_days = int(input("How many days's temperature? "))
counter = 0
history_of_temp = []
while counter<= numbers_of_days:
    counter += 1
    history_of_temp.append(int(input(f"Day {counter} hight temp: ")))

avg = sum(history_of_temp)/numbers_of_days
print(f"Average = {avg}")

for i in history_of_temp:
    if avg > i:
        print(f"{i} days(s) above average")