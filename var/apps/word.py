import tkinter as tk
from tkinter import font, colorchooser

def kalin_yap():
    suanki_font = font.Font(metin, metin.cget("font"))
    if suanki_font.actual()["weight"] == "normal":
        metin.configure(font=(suanki_font.actual()["family"], 12, "bold"))
    else:
        metin.configure(font=(suanki_font.actual()["family"], 12, "normal"))

pencere = tk.Tk()
pencere.title("Mini Word")
pencere.geometry("600x400")

# Araç Çubuğu
arac_cubugu = tk.Frame(pencere, bg="lightgrey")
arac_cubugu.pack(side="top", fill="x")

tk.Button(arac_cubugu, text="B", font=("Arial", 10, "bold"), command=kalin_yap).pack(side="left", padx=5, pady=5)
tk.Button(arac_cubugu, text="Sola Yasla", command=lambda: metin.tag_configure("left", justify='left')).pack(side="left")

metin = tk.Text(pencere, font=("Arial", 12), undo=True)
metin.pack(expand=True, fill="both")

pencere.mainloop()