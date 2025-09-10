import random
start_button = input('Type "start" or "exit":\n >> ').lower()
counts = 0

orders = []
while True:
    user_choice = input('Type "new","next","reset" or "exit": \n >> ')
    match user_choice :
        case "new":
            user_name = input("Please Enter your name:\n >> ")
            if user_name :
                if user_name not in orders:
                    orders.append(user_name)
                    token_counter = random.randint(101,200)
                    print(f'{user_name} your token number is {token_counter} in on the way...\n') 
                else:
                    print(f"{user_name} is exists in order, please try again \n")


        case "next":
            if not counts == len(orders):
                current_name = orders[counts]
                print(f"{current_name}, your order is ready.\n")
                counts +=1
            else:
                print("No more orders in the queue.\n")


        case "reset":
            if counts != len(orders):
                print("orders are pending\n")
                continue
            else:
                token_counter = 0
                print("Token counts are reset successfully.\n")
                start_button = "start"
            
        case "exit":
            if counts != len(orders):
                print("orders are pending\n")
                continue
            else:
                break
        case _:
            print(f"Invalid Entry {user_choice}\n")
            break
        
print(f"Today total customer has came {len(orders)}, List of customer {orders}")
        