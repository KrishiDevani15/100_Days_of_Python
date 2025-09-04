"""
A tea stall offers different prices for different cup sizes.
Write a program that calculates the price based on size.

Task:
    1) Take cup size input (small, medium, large)
    2) Small --> 10 rupees , Medium --> 15 rupees, Large --> 20 rupees
    3) If invalid: show "Unknown Cup Size"
"""

cup_size = input("Welcome to the tea stall! What cup size would you like (small, medium, large)? ").lower()
if (cup_size =="small"):
    print("The price for a small cup of tea is 10 rupees.")
elif (cup_size == "medium"):
    print("The price for a medium cup of tea is 15 rupees.")
elif (cup_size == "large"):
    print("The price for a large cup of tea is 20 rupees.")
else:
    print("Unknown Cup Size")