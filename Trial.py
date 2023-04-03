import tkinter as tk
import re
import hashlib

def check_password_strength(password, min_length=8, min_digits=1, min_special_chars=1, blacklist=[]):
    # Check length of password
    if len(password) < min_length:
        raise ValueError(f"Password is too short. It must be at least {min_length} characters long.")

    # Check for numeric characters
    if len(re.findall(r"\d", password)) < min_digits:
        raise ValueError(f"Password is too weak. It must contain at least {min_digits} digits.")

    # Check for special characters
    special_chars = re.findall(r"[^\w\s]", password)
    if len(special_chars) < min_special_chars:
        raise ValueError(f"Password is too weak. It must contain at least {min_special_chars} special characters.")

    # Check for blacklisted passwords
    for blacklisted_password in blacklist:
        if password == blacklisted_password:
            raise ValueError("Password is blacklisted. Please choose a different password.")

    # Check for common passwords
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.read().splitlines()
    if password.lower() in common_passwords:
        raise ValueError("Password is too common. Please choose a different password.")

    # Calculate password strength
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    score = 0
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1
    if len(special_chars) >= 2:
        score += 1
    if len(re.findall(r"\d", password)) >= 2:
        score += 1
    if hash_value in common_passwords:
        score -= 1

    return score

def check_password():
    try:
        password = password_entry.get()
        score = check_password_strength(password)
        if score >= 3:
            result_label.config(text="Password is strong!", fg="green")
        else:
            result_label.config(text=f"Password strength score is {score}. Please choose a stronger password.", fg="red")
    except ValueError as e:
        result_label.config(text=str(e), fg="red")

# Create tkinter window
window = tk.Tk()
window.title("Password Checker")
window.geometry("400x200")
window.config(bg="#1E90FF")

# Create password entry box
password_label = tk.Label(text="Enter Password:", bg="#1E90FF", fg="white")
password_label.pack()
password_entry = tk.Entry(width=30, show="*")
password_entry.pack()

# Create check button
check_button = tk.Button(text="Check Password", command=check_password, bg="#ffd700", fg="black")
check_button.pack()

# Create result label
result_label = tk.Label(text="", bg="#1E90FF", fg="white")
result_label.pack()

# Run tkinter window
window.mainloop()
