"""
A tea stall owner has a digital token display.
For every customer in line, a token number is printed and chai is served.
Task 
    1) Use a `for` loop to generate token number from 1 to 10 using `range()`
    2) Print: "Serving chai to Token #[number]"
"""
import time
for token in range(1,11):
    time.sleep(5)
    print(f"Serving chai to Token #{token}")
