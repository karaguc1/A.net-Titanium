from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
#os.system("killall python3 giris.py &")
ps=50
bs="red"
# Ana pencere oluşturma
p = tk.Tk()
p.geometry("1920x1080")
p.title("Geylani Desktop v15")
p.resizable(True, True)

# Arka plan resmi
try:
    bg_image = Image.open("/home/user/kernel/icons/arkaplan.png")
    bg_image = bg_image.resize((1920, 1080), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(p, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except FileNotFoundError:
    # Arka plan resmi bulunamazsa düz renk arka plan
    bg_label = tk.Label(p, bg="#1e3c72")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    print("Arka plan resmi bulunamadı")

# Saat ve tarih güncelleme
def update_time():
    current_time = datetime.now()
    time_label.config(text=f"{current_time.strftime('%d/%m/%Y')}\n{current_time.strftime('%H:%M:%S')}")
    p.after(1000, update_time)

# Menü yönetimi
menu_visible = False

def toggle_menu():
    """Menüyü açıp kapatan fonksiyon"""
    global menu_visible
    global tk_aico1  # Resim referansını global olarak tanımla
    
    try:
        # Resmi yükle (sadece ilk seferde)
        if not hasattr(toggle_menu, 'tk_aico1'):
            aico1 = Image.open("/home/user/kernel/icons/smi.ico")
            aico1 = aico1.resize((64, 64), Image.LANCZOS)
            toggle_menu.tk_aico1 = ImageTk.PhotoImage(aico1)  # Fonksiyon özelliği olarak sakla
        
        tk_aico1 = toggle_menu.tk_aico1
        
        if menu_visible:
            menu_frame.place_forget()
            menu_button.config(image=tk_aico1, text="")
        else:
            menu_frame.place(x=550, y=200)
            menu_button.config(image=tk_aico1, text="")
        
        menu_visible = not menu_visible
    
    except FileNotFoundError:
        # Resim bulunamazsa metin kullan
        if menu_visible:
            menu_frame.place_forget()
            menu_button.config(text="\nBaşlat\n")
        else:
            menu_frame.place(x=550, y=200)
            menu_button.config(text="\nMenü Kapat\n")
        menu_visible = not menu_visible
def poweroff():
    os.system("python3 /home/user/kernel/shd.py &")

def reboot():
    os.system("python3 /home/user/kernel/rbt.py &")

def logout():
    os.system("pkill -KILL -u $USER")

def arminal():
    os.system("bash -c 'gnome-terminal -- /usr/bin/python3 /home/user/kernel/arminal.py'")

def lock_screen():
    os.system("python3 /home/user/kernel/giris.py &")
    exit(1)
# Saat ve tarih etiketi
time_label = tk.Label(p, text="", fg="white", bg='#1a1a2e', font=("Arial", 10))
time_label.place(x=1280, y=640)

# İnternet butonu
try:
    internet_icon = Image.open("/home/user/kernel/icons/internetunknow.ico")
    internet_icon = internet_icon.resize((64, 64), Image.LANCZOS)
    tk_internet_icon = ImageTk.PhotoImage(internet_icon)
    internet_button = ttk.Button(p, image=tk_internet_icon, command=lambda: None)
    internet_button.image = tk_internet_icon  # Referansı koru
    internet_button.place(x=1200, y=710)
except FileNotFoundError:
    # İnternet ikonu bulunamazsa metin butonu
    internet_button = ttk.Button(p, text="İnternet", command=lambda: None)
    internet_button.place(x=500, y=450)
    print("İnternet ikonu bulunamadı")

# Menü çerçevesi
menu_frame = tk.Frame(p, bg="blue", bd=2, relief=tk.RAISED)

# Menü öğeleri
menu_items = [
    ("Shutdown", poweroff),
    ("Restart", reboot),
    ("Log out",lock_screen )
]

for text, command in menu_items:
    btn = ttk.Button(
        menu_frame, 
        text=text, 
        width=15, 
        command=command,
        style="Menu.TButton"
    )
    btn.pack(pady=5, padx=10, fill=tk.X)

# Stil tanımları
style = ttk.Style()
style.configure("Menu.TButton", 
               foreground="black", 
            #    background="#16213e", 
               font=("Arial", 10))
style.configure("TButton", 
               font=("Arial", 10),
               padding=5)

# Arama kısmı
search_entry = ttk.Entry(menu_frame, width=25, font=("Arial", 10))
search_entry.pack(pady=5, padx=10, fill=tk.X)

search_button = ttk.Button(
    menu_frame, 
    text="Search", 
    command=lambda: None,
    style="Menu.TButton"
)
search_button.pack(pady=5, padx=10, fill=tk.X)

#start button design
internet_ic = Image.open("/home/user/kernel/icons/smi.ico")
internet_ic = internet_ic.resize((64, 64), Image.LANCZOS)
tk_internet_ic = ImageTk.PhotoImage(internet_ic)
menu_button = ttk.Button(p, text="",image=tk_internet_ic, command=toggle_menu)
menu_button.place(x=0, y=710)
menu_button.image = tk_internet_ic  # Referansı koru
#pc button design
pcph = Image.open("/home/user/kernel/icons/Ekran Alıntısı.ico")
pcph = pcph.resize((64, 64), Image.LANCZOS)
tk_pcph = ImageTk.PhotoImage(pcph)
pca_button = ttk.Button(p, text="",image=tk_pcph, command=toggle_menu)
pca_button.place(x=0, y=0)
pca_button.image = tk_pcph
pc_label = tk.Label(p, text="This pc", fg="black",  font=("Arial", 13, "bold"))
pc_label.place(x=0, y=82)
#trashbox design
ckrs = Image.open("/home/user/kernel/icons/ckts.png")
ckrs = ckrs.resize((64, 64), Image.LANCZOS)
tk_ckrs = ImageTk.PhotoImage(ckrs)
aca_button = ttk.Button(p, text="",image=tk_ckrs, command=toggle_menu)
aca_button.place(x=0, y=120)
aca_button.image = tk_ckrs
aca_label = tk.Label(p, text="Trash", fg="black",  font=("Arial", 13, "bold"))
aca_label.place(x=15, y=203)
#file manager design
def fma():
    os.system("python3 /home/user/kernel/fmngr.py")
erpg = Image.open("/home/user/kernel/icons/er.png")
erpg = erpg.resize((64, 64), Image.LANCZOS)
tk_erpg = ImageTk.PhotoImage(erpg)
aca_button = ttk.Button(p, text="",image=tk_erpg, command=fma)
aca_button.place(x=300, y=710)
aca_button.image = tk_erpg
#web browser dedsign
def wba():
    #if you want use embeded web browser (not recommend) uncomment line 181 comment line 182  
    #os.system("python3 /home/user/kernel/webb.py")
    os.system("firefox-esr &")
wbpg = Image.open("/home/user/kernel/icons/webb.png")
wbpg = wbpg.resize((64, 64), Image.LANCZOS)
tk_wbpg = ImageTk.PhotoImage(wbpg)
wbb_button = ttk.Button(p, text="",image=tk_wbpg, command=wba)
wbb_button.place(x=400, y=710)
wbb_button.image = tk_wbpg
#settings design
def aa():
    os.system("python3 /home/user/kernel/ayarlar.py")
aapg = Image.open("/home/user/kernel/icons/ayar.png")
aapg = aapg.resize((64, 64), Image.LANCZOS)
tk_aapg = ImageTk.PhotoImage(aapg)
aa_button = ttk.Button(p, text="",image=tk_aapg, command=aa)
aa_button.place(x=500, y=710)
aa_button.image = tk_aapg
#hesap makinesi tasarımı
def hmac():
    os.system("python3 /home/user/kernel/hm.py")
hmico = Image.open("/home/user/kernel/icons/hm.ico")
hmico = hmico.resize((64, 64), Image.LANCZOS)
tk_hmico = ImageTk.PhotoImage(hmico)
hm_button = ttk.Button(p, text="",image=tk_hmico, command=hmac)
hm_button.place(x=200, y=710)
hm_button.image = tk_hmico
#mp4/mp3 çalar tasarımı
def mppac():
    os.system("python3 /home/user/kernel/mpp.py")
mppico = Image.open("/home/user/kernel/icons/sesic.png")
mppico = mppico.resize((64, 64), Image.LANCZOS)
tk_mppico = ImageTk.PhotoImage(mppico)
mppa_button = ttk.Button(p, text="",image=tk_mppico, command=mppac)
mppa_button.place(x=600, y=710)
mppa_button.image = tk_mppico
# Sürüm etiketi
# version_label = tk.Label(p, text="Bozkurt Desktop v5", fg="black",  font=("Arial", 10, "bold"))
# version_label.place(x=1000, y=0)

# Ayırıcı çizgi
separator = tk.Label(p, bg="#0f3460", height=1)
separator.place(x=0, y=690, relwidth=1)
# Ayırıcı çizgi
separator1 = tk.Label(p, bg="#0f3460", height=5)
separator1.place(x=90, y=690, relwidth=0)
separator2 = tk.Label(p, bg="#0f3460", height=5)
separator2.place(x=940, y=690, relwidth=0)
aico = Image.open("/home/user/kernel/icons/arminal.ico")
aico = aico.resize((64, 64), Image.LANCZOS)
tk_aico = ImageTk.PhotoImage(aico)
#ses butonu tasarımı
sbico = Image.open("/home/user/kernel/icons/Adsıza.png")
sbico = sbico.resize((64, 64), Image.LANCZOS)
tk_sbico = ImageTk.PhotoImage(sbico)
ses_button = ttk.Button(p, text="",image=tk_sbico, command=None)
ses_button.place(x=1115, y=710)
ses_button.image = tk_sbico
#bluetooh butonu tasarımı
blico = Image.open("/home/user/kernel/icons/bltth.png")
blico = blico.resize((64, 64), Image.LANCZOS)
tk_blico = ImageTk.PhotoImage(blico)
blt_button = ttk.Button(p, text="",image=tk_blico, command=None)
blt_button.place(x=945, y=710)
blt_label = tk.Label(p, text="__", fg=bs,bg=bs, font=("Arial", 8))
blt_label.place(x=945, y=760)
blt_button.image = tk_blico
#pil tasarımı
pilico = Image.open("/home/user/kernel/icons/pil.png")
pilico = pilico.resize((64, 64), Image.LANCZOS)
tk_pilico = ImageTk.PhotoImage(pilico)
pil_button = ttk.Button(p, text="",image=tk_pilico, command=None)
pil_button.place(x=1030, y=710)
pil_button.image = tk_sbico
pil_label = tk.Label(p, text=f"%{ps}", fg="black",bg="white", font=("Arial", 8))
pil_label.place(x=1050, y=760)
# Terminal butonu
terminal_button = ttk.Button(
    p, 
    #text="Arminal\n___\n|>  |\n---", 
    command=arminal,
    style="Terminal.TButton",
    image=tk_aico
)
aico.image = tk_aico  # Referansı koru
style.configure("Terminal.TButton", 
               foreground="white", 
            #    background="#16213e", 
               font=("Courier", 9))
terminal_button.place(x=100, y=710)

# Saat güncellemesini başlat
update_time()

# Ana döngüyü başlat
p.mainloop()
