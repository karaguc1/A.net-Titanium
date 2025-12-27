import tkinter as tk
from tkinter import ttk
import os
import platform
from colorama import Fore, Style
# Dinamik ana dizin belirleme
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Kullanıcı verileri için yol (Windows/Linux uyumlu)
USER_DATA_PATH = os.path.join(BASE_DIR, "set", "secret", "ring", "0")

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A.net Giriş")
        self.root.geometry("400x300")
        
        # Stil tanımlamaları
        style = ttk.Style()
        style.configure("Rounded.TButton", padding=5)

        self.label1 = tk.Label(root, text="Kullanıcı Adı", font=("Arial", 10))
        self.label1.pack(pady=5)
        self.kadi_entry = ttk.Entry(root, width=25)
        self.kadi_entry.pack(pady=5)

        self.label2 = tk.Label(root, text="Şifre", font=("Arial", 10))
        self.label2.pack(pady=5)
        self.sifre_entry = ttk.Entry(root, width=25, show="*")
        self.sifre_entry.pack(pady=5)

        self.giris_button = ttk.Button(root, text="Giriş Yap", command=self.giris_yap)
        self.giris_button.pack(pady=20)
        
        self.bilgi_label = tk.Label(root, text="", font=("Arial", 9))
        self.bilgi_label.pack()
        print(Fore.BLUE + "==============Metaui v5==============" + Fore.RESET)
        print("[",Fore.BLUE + "INFO" + Fore.RESET + "]",Fore.YELLOW + "Metaui v5 started..." + Fore.RESET)
        print("[",Fore.BLUE + "INFO" + Fore.RESET + "]",Fore.YELLOW + "waiting for login..." + Fore.RESET)
    def giris_yap(self):
        kullanici = self.kadi_entry.get()
        sifre = self.sifre_entry.get()
        
        if not kullanici or not sifre:
            self.bilgi_label.config(text="Eksik bilgi!", fg="red")
            return

        # Hibrit dosya kontrolü
        user_file = os.path.join(USER_DATA_PATH, f"{kullanici}.usr")
        
        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                saved_pass = f.read().strip()
            
            if sifre == saved_pass:
                self.bilgi_label.config(text="Giriş Başarılı!", fg="green")
                print("[",Fore.GREEN + "OK" + Fore.RESET + "]",Fore.GREEN + "login successfully!" + Fore.RESET)
                print("[",Fore.BLUE + "INFO" + Fore.RESET + "]",Fore.YELLOW + f"creating user space for '{kullanici}'..." + Fore.RESET)
                from memman import MemMan
                fs = MemMan(kullanici)
                fs.create_folder("Documents")
                fs.create_folder("Desktop")
                fs.create_folder("Downloads")
                fs.create_folder("Videos")
                fs.create_folder("Photos")
                fs.create_folder("Musics")
                # Masaüstünü başlat (Windows/Linux uyumlu)
                self.root.destroy()
                os.system(f"python {os.path.join(BASE_DIR, 'desk.py')}")
            else:
                self.bilgi_label.config(text="Hatalı Şifre!", fg="red")
        else:
            self.bilgi_label.config(text="Kullanıcı bulunamadı.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()