"""
Age Verification System
You’re building a system to verify user age for access.

Tasks:
    1) Define a function verify_age that accepts a string input named age_str.
    2) Convert age_str to an integer using int().
    3) Use a ternary operator to return:
        "Access Granted" if age is 18 or older
        "Access Denied" otherwise
"""
age = int(input("Enter your age: "))
verify_age = "Access Granted" if age >=18 else "Access Denied"
print(f" Your are :- {verify_age}.")