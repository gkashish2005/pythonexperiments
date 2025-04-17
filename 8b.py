#NAME: KASHISH GUPTA 231P081/09 SECOMPS A
"""Write a python program to create entry widgets for entering username and password and display entered text."""
import tkinter as tk
from tkinter import messagebox
# Function to display entered text
def display_text():
    username = entry_username.get()
    password = entry_password.get()
    messagebox.showinfo("Entered Information", f"Username: {username}\nPassword: {password}")
# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")
# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)
# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)
# Submit button
button_submit = tk.Button(root, text="Submit", command=display_text)
button_submit.pack(pady=10)
# Run the main event loop
root.mainloop()
