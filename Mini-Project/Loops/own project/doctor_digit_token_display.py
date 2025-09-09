start_button = input('Type "start" or "exit":\n >> ').lower()
token_counter = 0

while start_button!="exit":
    user_choice = input('Type "next","reset" or "exit": \n')
    match user_choice :
        case "next":
            token_counter+= 1
            print(f"Token #{token_counter} please come.")
            
        case "reset":
            token_counter = 0
            print("Token counts are reset successfully.")
            start_button = "start"
            
        case "exit":
            break
        
        case _:
            print(f"Invalid Entry {user_choice}")
            break
        
print(f"Today total patient has came {token_counter}")