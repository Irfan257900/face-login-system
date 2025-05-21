import tkinter as tk
from tkinter import simpledialog, messagebox
from register import register_user
from login import login_user

def handle_register():
    name = simpledialog.askstring("Register", "Enter your name:")
    if name:
        register_user(name)
        messagebox.showinfo("Success", f"User {name} registered!")

def handle_login():
    result = login_user()
    if result != "Login Failed" and result != "No data":
        messagebox.showinfo("Success", f"Welcome back, {result}!")
    else:
        messagebox.showerror("Failed", "Face not recognized.")

# GUI
root = tk.Tk()
root.title("Face Login System")
root.geometry("300x200")

tk.Label(root, text="Face Recognition Login", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Register", width=20, command=handle_register).pack(pady=10)
tk.Button(root, text="Login", width=20, command=handle_login).pack(pady=10)

root.mainloop()
