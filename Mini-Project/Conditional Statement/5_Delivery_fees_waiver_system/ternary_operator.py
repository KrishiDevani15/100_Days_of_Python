"""
You run an online tea store.
if the order amount is more than 300 rupees, the delivery fee.
Otherwise, it costs 30 rupees.

Task:
    1. Input: `order_amount`
    2. Use a ternary operator to decide delivery fee.
"""
order_amount = int(input("Enter the order amount: "))
delivery_fee = 0 if order_amount > 300 else 30
print(f"Delivery fee is : {delivery_fee} rupees")