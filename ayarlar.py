import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
def init():
    p.mainloop()
p = tk.Tk()
p.geometry("450x450")
p.title("Settings")
p.resizable(True, False)
internet_ic = Image.open("/home/user/kernel/icons/ayar.png")
internet_ic = internet_ic.resize((64, 64), Image.LANCZOS)
tk_internet_ic = ImageTk.PhotoImage(internet_ic)
menu_button = tk.Label(p, text="",image=tk_internet_ic)
menu_button.place(x=0, y=0)
def chzsek():
    None
def hspsek():
    None
def pcsek():
    None
def netsek():
    None
def zmnsek():
    None
def dlsek():
    None
def gncsek():
    None
def erssek():
    None
def gzlsek():
    None
def krtsek():
    None
def versek():
    os.system("python3 /home/user/kernel/aver.py")


chzset_button = ttk.Button(p, text="Devices",command=chzsek)
chzset_button.place(x=0, y=70)
pcset_button = ttk.Button(p, text="Computer",command=pcsek)
pcset_button.place(x=0, y=100)
netset_button = ttk.Button(p, text="Network",command=netsek)
netset_button.place(x=0, y=130)
zmnset_button = ttk.Button(p, text="Time",command=zmnsek)
zmnset_button.place(x=0, y=160)
dlset_button = ttk.Button(p, text="Language",command=dlsek)
dlset_button.place(x=0, y=190)
gzlset_button = ttk.Button(p, text="Security",command=gzlsek)
gzlset_button.place(x=0, y=220)
krtset_button = ttk.Button(p, text="Recovery",command=krtsek)
krtset_button.place(x=0, y=250)
gncset_button = ttk.Button(p, text="Update",command=gncsek)
gncset_button.place(x=0, y=280)
ersset_button = ttk.Button(p, text="Accessbility",command=erssek)
ersset_button.place(x=0, y=310)
hspset_button = ttk.Button(p, text="Accounts",command=hspsek)
hspset_button.place(x=0, y=340)
hspset_button = ttk.Button(p, text="Versiyon",command=versek)
hspset_button.place(x=0, y=370)
separator1 = tk.Label(p, bg="#0f3460", height=50)
separator1.place(x=100, y=0, relwidth=0)
init()
