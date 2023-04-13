import tkinter as tk

def check_password_strength(password):
    if len(password) < 8:
        return 'Password is too short'
    elif not any(char.isdigit() for char in password):
        return 'Password should have at least one numeral'
    elif not any(char.isupper() for char in password):
        return 'Password should have at least one uppercase letter'
    elif not any(char.islower() for char in password):
        return 'Password should have at least one lowercase letter'
    elif not any(char in '@_!#$%^&*()<>?/\\|}{~:' for char in password):
        return 'Password should have at least one special character'
    else:
        return 'Password is strong'

def check_password():
    password = entry.get()
    result = check_password_strength(password)
    result_label.config(text=result)

window = tk.Tk()
window.title("Password Checker")
window.geometry("400x200")
window.config(bg="#1E90FF")

# Create password entry box
label = tk.Label(text="Enter Password:", bg="#1e91ff", fg="white")
label.pack(padx=5, pady=8)
entry = tk.Entry(width=30, show="")
entry.pack(padx=5, pady=8)

# Create check button
check_button = tk.Button(text="Check Password", command=check_password, bg="#ffd700", fg="black")
check_button.pack(padx=5, pady=7)

# Create result label
result_label = tk.Label(text="", bg="#1e91ff", fg="white")
result_label.pack(padx=5, pady=25, side=tk.BOTTOM)

# Run tkinter window
window.mainloop()
