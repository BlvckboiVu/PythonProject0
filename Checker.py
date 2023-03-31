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
    Function to check the strength of a password.

    Password must be over 8 characters and must contain alphanumeric, upper and lowercase characters.

    Args:
        password (str): The password to be checked.
Returns:
        int: 0 if password is weak, 1 if password is moderate, 2 if password is strong.
    """
    # Initialize strength score to 0
    strength = 0

    # Check password length
    if len(password) < 8:
        print("Password is weak. It must be at least 8 characters long.")
        return strength

   # Check for alphanumeric characters
    if not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
        print("Password is weak. It must contain alphanumeric characters.")
        return strength

    # Check for uppercase and lowercase characters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        print("Password is moderate. It should contain both uppercase and lowercase characters.")
        strength = 1
    else:
        strength = 2

    # Return strength score
    return strength

# Keep asking for password until a strong password is entered
