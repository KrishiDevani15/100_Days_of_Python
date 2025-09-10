"""
zip(*iterables, strict= False) --> Iterate over several iterables in parallel,producting tuples with an item from each one.

You're preparing an order summary with customer names asn their total bill.
Task:
    1) Use two lists: one for names and one for bills
    2) Print: "[Name] paid [amount] rupees"  
"""
names = ["Hitesh","Meera","Sam","Ali"]
bills = [50,70,100,55]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")