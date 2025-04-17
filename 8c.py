#NAME: KASHISH GUPTA 231P081/09 SECOMPS A
"""Write a python GUI password protected program."""
import tkinter as tk
from tkinter import messagebox
# Predefined username and password
USERNAME = "admin"
PASSWORD = "password123"
# Function to check credentials
def check_login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()
    if entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login Successful", "Access Granted!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")
# Create main window
root = tk.Tk()
root.title("Password Protected Login")
root.geometry("300x200")
# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)
# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
\entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)
# Submit button
button_submit = tk.Button(root, text="Login", command=check_login)
button_submit.pack(pady=10)
# Run the main event loop
root.mainloop()
