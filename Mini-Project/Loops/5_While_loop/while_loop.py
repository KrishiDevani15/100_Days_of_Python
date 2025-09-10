"""
You want to simulate tea heating.
Its starts at 40c and boils at 100c
Task:
    1) Use a `while` loop.
    2) Increase temperature by 15 until it reaches or exceeds 100.
    3) Print each temperature step.
"""
temperature = 100
while temperature < 100:
    print(f"Current temperature: {temperature}")
    temperature += 15

print("Tea is ready to boil")