"""
You're creating a tea menu board.
Eaxh item must be numbered.
Task:
    1) Use `enumerate()` to print menu items with numbers.
"""

menu = ["Green","Lemon","Spiced","Mint"]

for idx, item in enumerate(menu):
    print(f"{idx} : {item} chai")