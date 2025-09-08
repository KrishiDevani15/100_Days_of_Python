print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on the pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra chesse ? Y or N: ").lower()
price = 0 

match size:
    case "s":
        price = 15
    case "m":
        price = 20
    case "l":
        price = 25
    case _:
        print("Invalid Pizza Size")

if (pepperoni == 'y'):
    if (size == 's'):
        price+=2
    else:   
        price+=3
        
if extra_cheese == 'y':
    price+=1

print(f"Final bill will be {price}")