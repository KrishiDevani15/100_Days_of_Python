# Calculate displacement (d = v^2 - u^2 / 2a)
u = int(input("Enter initial velocity (u) in m/s: "))
v = int(input("Enter final velocity (v) in m/s: "))
a = int(input("Enter acceleration (a) in m/s^2: "))

# Expression
s = (v*v - u*u) / (2 * a)
print(f"Displacement (s) is: {s} meters")