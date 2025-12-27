import tkinter as tk
from tkinter import ttk
import os
root=tk.Tk()
root.title("Add user")
root.geometry("400x300")
label1 = tk.Label(root, text="New users name", fg="black", font=("Arial", 10))
label1.pack()
kadi_entry = ttk.Entry(root, width=25, style="TEntry")
kadi_entry.pack(pady=8)
label2 = tk.Label(root, text="New users password", fg="black", font=("Arial", 10))
label2.pack(pady=10)
sifre_entry = ttk.Entry(root, width=25, show="*", style="TEntry")
sifre_entry.pack(pady=12)
label2 = tk.Label(root, text="New users password again", fg="black", font=("Arial", 10))
label2.pack(pady=14)
sifre_entry2 = ttk.Entry(root, width=25, show="*", style="TEntry")
sifre_entry2.pack(pady=16)
def giris_yap():
    user=kadi_entry.get()
    pass1=sifre_entry.get()
    pass2=sifre_entry2.get()
    if pass1==pass2:
        open(f"/home/user/kernel/set/secret/ring/0/{user}.usr", "x")
        with open("/home/user/kernel/set/secret/ring/0/user.usr", "a") as f:
            f.write(f",{user}")
        with open(f"/home/user/kernel/set/secret/ring/0/{user}.usr", "w") as f:
            f.write(f"{pass1}")
        exit(5)
    else:
        None
giris_button = ttk.Button(root, text="Kullanıcı oluştur",style="Rounded.TButton",command=giris_yap)
giris_button.pack(pady=18)
root.mainloop()
