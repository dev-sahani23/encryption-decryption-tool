import tkinter as tk
from tkinter import messagebox
import random
import string

# Character set
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)

# Encrypt function
def encrypt():
    plain_text = text_input.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not plain_text or not password:
        messagebox.showerror("Error", "Please enter both text and password.")
        return

    random.seed(password)
    key = chars.copy()
    random.shuffle(key)

    cipher_text = ""
    for char in plain_text:
        if char in chars:
            cipher_text += key[chars.index(char)]
        else:
            cipher_text += char  # Keep unknown chars as-is

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, cipher_text)

# Decrypt function
def decrypt():
    cipher_text = text_input.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not cipher_text or not password:
        messagebox.showerror("Error", "Please enter both text and password.")
        return

    random.seed(password)
    key = chars.copy()
    random.shuffle(key)

    plain_text = ""
    for char in cipher_text:
        if char in key:
            plain_text += chars[key.index(char)]
        else:
            plain_text += char  # Keep unknown chars as-is

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, plain_text)

# GUI Setup
root = tk.Tk()
root.title("Text Encryptor & Decryptor")
root.geometry("500x500")
root.config(padx=20, pady=20)

# Widgets
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack()
text_input = tk.Text(root, height=5, width=60)
text_input.pack()

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=(10, 0))
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack()

tk.Button(root, text="Encrypt", command=encrypt, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)
tk.Button(root, text="Decrypt", command=decrypt, bg="#2196F3", fg="white", padx=10, pady=5).pack(pady=(0, 10))

tk.Label(root, text="Output:", font=("Arial", 12)).pack()
output_text = tk.Text(root, height=5, width=60)
output_text.pack()

root.mainloop()