print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price = 0
if height >=120 :
    print("You can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age<12:
        price = 5
        print("Child tickets are $5.")
    elif age<18:
        price = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on use!")
    else:
        price = 12
        print("Adult tickets are $12.")

    # Multiple if statement in succession
    wants_photo = input("Do your want to have a photo take? Type y for Yes and n for No. ").lower()
    if wants_photo == "y":
        price +=3
    
    print(f"Total bill is ${price}")

else:
    print("Sorry you have to grow taller before you can ride.")