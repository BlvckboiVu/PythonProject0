 import re
password = input("Enter password: ")

has_uppercase = False
has_number = False

if len(password) >= 8:
    for c in password:
        if c.isupper():
            has_uppercase = True
        elif c.isdigit():
            has_number = True

    if has_uppercase and has_number:
        print("Strong password!")
    elif has_uppercase or has_number:
        print("Moderate password!")
    else:
        print("Weak password!")
else:
    print("Password must be at least 8 characters long!")
import re

def check_password_strength(password):
    """
    Function to check the strength of the password.

    Password must be over 8 characters and must contain alphanumeric, upper and lowercase characters.

    Args:
        password (str): The password to be checked.
