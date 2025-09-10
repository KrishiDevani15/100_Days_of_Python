import time

user_choice = input('Type "start" or "exit":\n >> ').lower()

if user_choice == "start":
    traffic_light = 'red'
    last_light = False

    while True:

        if traffic_light == "red":
            print("Red light - wait 5 seconds")
            for i in range(5, 0, -1):
                print(i)
                time.sleep(1)
            traffic_light = "yellow"

        elif traffic_light == "yellow":
            print("Yellow light - wait 2 seconds")
            for i in range(2, 0, -1):
                print(i)
                time.sleep(1)
            if not last_light:
                traffic_light = 'green'
            else:
                traffic_light = 'red'
            
            last_light = not last_light

        elif traffic_light == "green":
            print("Green light - wait 5 seconds")
            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)
            traffic_light= "yellow"


elif user_choice == "exit":
    print("Exiting program.")
else:
    print("Invalid input.")
