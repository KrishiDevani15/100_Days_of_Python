import random
letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
letters_password = int(input("How many letters would you like in your password?\n >> "))
symbols_password = int(input("How many symbols would you like?\n >> "))
number_password = int(input("How many numbers would you like?\n >> "))

password_list = []
for char in range(0,letters_password):
    password_list.append(random.choice(letters))

for symbol in range(0,symbols_password):
    password_list.append(random.choice(symbols))

for num in range(0,number_password):
    password_list.append(random.choice(number))

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for character in password_list:
    password += str(character)

print(f"Your password is: {password}")