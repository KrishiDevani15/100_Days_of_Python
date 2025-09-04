"""
A local cafe wants a program that suggests a snack.
If a customer asks for cookies or samosa, if confirm the order.
Otherwise, it says it's not available.

Task:
    1) Take snack input
    2) If the snack is `cookies`or `samosa`, confirm the order
    3) Else, show `unavailability`

"""

snack = input("Welcome to the local cafe! What snack would you like to order? ").lower()
if (snack == "cookies" or snack == "samosa"):
    print(f"Great Choice! Your order for {snack} has been confirmed.")
else:
    print(f"Sorry, we only serve cookies or samosa with tea. {snack} is not available.")