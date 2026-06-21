import tkinter as tk
from tkinter import messagebox
 
def read_file():
    try:
        file = open("users.txt", "r")
        data = file.read()
        file.close()
        return data
    except:
        return ""
 
def write_file(username, password):
    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()
 
def login():
    username = entry_user.get()
    password = entry_pass.get()
 
    data = read_file()
    lines = data.strip().split("\n")
 
    for line in lines:
        if line == username + "," + password:
            messagebox.showinfo("Success", "Login successful!")
            return
 
    messagebox.showerror("Error", "Invalid username or password.")
 
def signup():
    username = entry_user.get()
    password = entry_pass.get()
 
    data = read_file()
    lines = data.strip().split("\n")
 
    for line in lines:
        if line.split(",")[0] == username:
            messagebox.showerror("Error", "Username already exists.")
            return
 
    write_file(username, password)
    messagebox.showinfo("Success", "Account created successfully!")
 
def main():
    global entry_user, entry_pass
 
    tk.Label(root, text="Username:").pack(pady=5)
    entry_user = tk.Entry(root)
    entry_user.pack(pady=5)
 
    tk.Label(root, text="Password:").pack(pady=5)
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack(pady=5)
 
    tk.Button(root, text="Login", command=login).pack(pady=5)
    tk.Button(root, text="Signup", command=signup).pack(pady=5)
 
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")
 
main()
 
root.mainloop()