import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
p = tk.Tk()
p.geometry("450x63")
p.title("About A.net")
p.resizable(False, False)
def ok():
    p.destroy()
internet_ic = Image.open("icons/smi.ico")
internet_ic = internet_ic.resize((64, 64), Image.LANCZOS)
tk_internet_ic = ImageTk.PhotoImage(internet_ic)
menu_button = tk.Label(p, text="",image=tk_internet_ic)
menu_button.place(x=0, y=0)
menu1_button = tk.Label(p, text="A.net v2.0 (Merve)",fg="blue",font=("tahoma",15))
menu1_button.place(x=100, y=20)
# label_button = tk.Label(p, text="A.net beta",fg="black")
# label_button.place(x=100, y=50)
menu_button.image = tk_internet_ic  # Referansı koru
ok_button = ttk.Button(p, text="OK",command=ok)
ok_button.place(x=350, y=20)
p.mainloop()
