import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import jetpack  # Kendi yazdığımız motoru import ediyoruz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_path(name): return os.path.join(BASE_DIR, "icons", name)

class AppStore:
    def __init__(self, root):
        self.root = root
        self.root.title("A.net App Store")
        self.root.geometry("1000x700")
        self.root.configure(bg="#121212") # Dark mode

        # --- Yan Menü ---
        self.side_bar = tk.Frame(self.root, bg="#1e1e1e", width=220)
        self.side_bar.pack(side="left", fill="y")
        
        tk.Label(self.side_bar, text="A.net Store", fg="#007aff", bg="#1e1e1e", 
                 font=("Segoe UI", 18, "bold")).pack(pady=30)

        menu_items = ["Keşfet", "Uygulamalar", "Oyunlar", "Güncellemeler", "Ayarlar"]
        for item in menu_items:
            btn = tk.Button(self.side_bar, text=f"  {item}", fg="white", bg="#1e1e1e", 
                            font=("Segoe UI", 11), bd=0, anchor="w", cursor="hand2")
            btn.pack(fill="x", pady=5, padx=10)

        # --- Ana İçerik Alanı ---
        self.main_canvas = tk.Canvas(self.root, bg="#121212", highlightthickness=0)
        self.scroll_y = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.main_frame = tk.Frame(self.main_canvas, bg="#121212")

        self.main_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.scroll_y.set)

        self.main_canvas.pack(side="left", fill="both", expand=True, padx=20)
        self.scroll_y.pack(side="right", fill="y")

        self.load_featured_apps()

    def load_featured_apps(self):
        # Gerçekten kurulabilir paket listesi
        self.apps = [
            {"name": "Bozkurt Editör", "desc": "Gelişmiş Metin Düzenleyici", "icon": "folder.png", "pack": "editor_v1.aupac"},
            {"name": "Sistem Yaması", "desc": "Kernel 0.0.3 Güncellemesi", "icon": "ayar.png", "pack": "kernel_update.aupac"},
            {"name": "A.net Music", "desc": "MP3 Çalar ve Düzenleyici", "icon": "Adsıza.png", "pack": "music_app.aupac"},
            {"name": "Hava Durumu", "desc": "Anlık Hava Durumu Takibi", "icon": "smi.ico", "pack": "weather.aupac"}
        ]

        row, col = 0, 0
        for app in self.apps:
            self.create_app_card(app, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def create_app_card(self, app, r, c):
        card = tk.Frame(self.main_frame, bg="#1e1e1e", bd=0, padx=15, pady=15)
        card.grid(row=r, column=c, padx=15, pady=15)

        # İkon İşleme
        try:
            img = Image.open(get_path(app["icon"])).resize((80, 80), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_lbl = tk.Label(card, image=photo, bg="#1e1e1e")
            img_lbl.image = photo
            img_lbl.pack()
        except:
            tk.Label(card, text="📦", font=("Arial", 30), bg="#1e1e1e", fg="white").pack()

        tk.Label(card, text=app["name"], fg="white", bg="#1e1e1e", font=("Segoe UI", 12, "bold")).pack(pady=(10, 0))
        tk.Label(card, text=app["desc"], fg="#aaaaaa", bg="#1e1e1e", font=("Segoe UI", 9)).pack(pady=5)
        
        btn = tk.Button(card, text="YÜKLE", bg="#007aff", fg="white", font=("Segoe UI", 10, "bold"),
                        bd=0, padx=20, pady=5, cursor="hand2", command=lambda a=app: self.start_install(a))
        btn.pack(pady=10)

    def start_install(self, app_data):
        if messagebox.askyesno("Kurulum", f"{app_data['name']} kurulmaya başlansın mı?"):
            # Jetpack motorunu çağırıyoruz
            res = jetpack.jetpack_engine(app_data['pack'])
            if res:
                messagebox.showinfo("Başarılı", f"{app_data['name']} başarıyla sisteme entegre edildi.")
            else:
                messagebox.showerror("Hata", "Paket yüklenemedi! Dosya bozuk veya eksik.")

if __name__ == "__main__":
    root = tk.Tk()
    store = AppStore(root)
    root.mainloop()