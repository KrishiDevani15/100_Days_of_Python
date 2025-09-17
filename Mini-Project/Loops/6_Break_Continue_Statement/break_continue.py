'''
Some chai flavors are out of stock.
You want to skip those and stop entirely if someone requents a restricted flavor.

Task:
    1) Skip if flaour is `Out of Stock`
    2) Break if flavor is `Discontinued`
'''

flavours = ["Ginger","Out of Stock","Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    elif flavour == "Discontinued":
        break
    print(f"Available Flavour {flavour}")
print("Out side of Loop")
