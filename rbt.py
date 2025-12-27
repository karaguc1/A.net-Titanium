import tkinter as tk
import os
from time import *
root=tk.Tk()
root.title("Restart")
root.geometry("500x100")
label1 = tk.Label(root, text="Restarting...", fg="black", font=("Arial", 35))
label1.pack(pady=10)
root.mainloop()
sleep(2)
os.system("reboot")
