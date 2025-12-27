import tkinter as tk

class PaintUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Basit Paint")
        
        self.firca_rengi = "black"
        self.tuval = tk.Canvas(self.pencere, bg="white", width=800, height=600)
        self.tuval.pack(expand=True, fill="both")
        
        # Fare hareketlerini bağla
        self.tuval.bind("<B1-Motion>", self.ciz)
        
        # Renk Seçenekleri
        buton_cercevesi = tk.Frame(self.pencere)
        buton_cercevesi.pack(fill="x")
        
        renkler = ["black", "red", "blue", "green", "yellow"]
        for renk in renkler:
            tk.Button(buton_cercevesi, bg=renk, width=2, command=lambda r=renk: self.renk_degistir(r)).pack(side="left")
            
        tk.Button(buton_cercevesi, text="Temizle", command=lambda: self.tuval.delete("all")).pack(side="right")

    def ciz(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.tuval.create_oval(x1, y1, x2, y2, fill=self.firca_rengi, outline=self.firca_rengi)

    def renk_degistir(self, yeni_renk):
        self.firca_rengi = yeni_renk

root = tk.Tk()
PaintUygulamasi(root)
root.mainloop()