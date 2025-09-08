# Area of Cuboid is 2*(lw + lh + wh)
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

# Expression to calculate the area of the cuboid
area = 2 * (((length * width) + length * height) + width * height)
print("The area of the cuboid is:", area)