print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

is_verified_to_ride = "You can ride the rollercoaster" if (height >= 120) else "Sorry you have to grow taller before you can ride."
print(is_verified_to_ride)