import re

def check_password_strength(password):
   # To check if the length of the passwors is less than 8
    if len(password) < 8:
        return 'Password is too short'
   # To check if it has numerical characters
    elif not any(char.isdigit() for char in password):      
        return 'Password should have at least one numeral'
   # To chack if it has Uppercase characters
    elif not any(char.isupper() for char in password):
        return 'Password should have at least one uppercase letter'
   # To check if it has lowercase characters
    elif not any(char.islower() for char in password):
        return 'Password should have at least one lowercase letter'
   # To check if it has special characters
    elif not any(char in '@_!#$%^&*()<>?/\\|}{~:' for char in password):
        return 'Password should have at least one special character'
    else:
        return 'Password is strong'
# The loop makes it so that it asks for input again if the password is not strong enough
while True:
    password = input('Enter a password: ')
    result = check_password_strength(password)
    print(result)
    if result == 'Password is strong':
        break
