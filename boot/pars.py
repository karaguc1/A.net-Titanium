import os
import subprocess
w=0
from time import *
import os
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
w=0

# Dosya listesi (orijinal haliyle korundu)
file_list = [
    "../addu.py",
    "../akrl.py",
    "../arminal.py",
    "../aver.py",
    "../ayarlar.py",
    "../connectornet.py",
    "../control.py",
    "../desk.py",
    "../diskmanager.py",
    "../fmngr.py",
    "../giris.py",
    "../hm.py",
    "../jetpack.py",
    "../kernel.py",
    "../mpp.py",
    "./pars.py",
    "./kinetic.py",
    "./diskmanager.py",
    "../r.arminal.py",
    "../rbt.py",
    "../readme.txt",
    "../root.jetpack.py",
    "../shd.py",
    "../webb.py",
]

def kernel_panic(missing_files):
    if isinstance(missing_files, (list, tuple)):
        missing_display = ', '.join(f'"{f}"' for f in missing_files)
        path_display = ','.join(missing_files)
    else:
        missing_display = f'"{missing_files}"'
        path_display = missing_files

    # Hata ekranını kırmızı ve dikkat çekici yaptım
    error_msg = rf"""
 {Fore.RED}{Style.BRIGHT}[!] CRITICAL SYSTEM ERROR: KERNEL_THREAD_NOT_HANDLED
 ----------------------------------------------------
 {Fore.WHITE}[ TIME ] {time.strftime("%Y/%m/%d %H:%M")}
 [ MODULE ] VFS_MOUNT_ROOT
 [ ERROR ] {Fore.YELLOW}MISSING: {missing_display}
   {Fore.RED}_________________________________________
  /                                         \\
 |                   [^]                     |
 |                 [/ __ \]                  |
 |                [/ |  | \]                 | 
 |               [/  |  |  \]                |
 |              [/   |  |   \]               |
 |             [/    |  |    \]              |
 |            [/     |  |     \]             |
 |           [/      |  |      \]            |
 |          [/       |__|       \]           |
 |         [/         __         \]          |
 |        [/         (__)         \]         |
 |       [/________________________\]        |
 |                                           |
 |                                           | 
 |   !   FATAL ERROR: SYSTEM HALTED  !       |
 |                                           |
 |   Reason: Initial process failed.         |
 |   Path: /kernel/{path_display}            |
 |                                           |
 |   [ ERR_CODE: 0xE344240404 ]              |
  \\_________________________________________/

 {Fore.LIGHTRED_EX}PANIC: Unable to mount root fs on unknown-block(0,0)
 please visit {Fore.CYAN}www.a.com/anet/errors/0xE344240404{Fore.LIGHTRED_EX} .
 {Fore.RED}----------------------------------------------------
    """
    print(error_msg)

def check_files(files):
    base_dir = os.path.dirname(__file__) or os.getcwd()
    missing = []
    for f in files:
        path = os.path.join(base_dir, f)
        if not os.path.exists(path):
            missing.append(f)

    if missing:
        kernel_panic(missing)
        exit(1)

sertificate=[".{00010001011110111001101001}@pard.{11101110100001000110010110}@pard.{01100110100100101000100001}@pard.{01110100000111101001111101}@pard?(11111111111111111111111111)@end![00000000000000000000000000]@endp"]

# Hoşgeldin ekranı
os.system("cls" if os.name == "nt" else "clear")
print(Back.BLUE + Fore.WHITE + Style.BRIGHT + " Welcome To Pars! ".center(40) + Style.RESET_ALL)
sleep(2)

def draw_header():
    print(Fore.CYAN + "================pars bootloader v15.0=================")

def msg(tur, met):
    if tur == 1:
        print(f"{Fore.BLUE}[ INFO ] {Fore.WHITE}{met}")
    elif tur == 2:
        print(f"{Fore.RED}{Style.BRIGHT}[ ERROR ] {Fore.YELLOW}{met}")   
    elif tur == 3:
        print(f"{Fore.GREEN}[ OK ] {Fore.WHITE}{met}")

os.system("cls" if os.name == "nt" else "clear")
draw_header()
sleep(1)        
msg(1, "Pars Bootloader 0.0.2")  
sleep(1)      
msg(1, "System Booting...")
sleep(2)  

a=0
# Spinner ve dosya kontrol döngüsü
while a < len(file_list) + 1:
    os.system("cls" if os.name == "nt" else "clear")
    draw_header()
    msg(1, "Pars Bootloader 0.0.2")  
    msg(1, "System Booting...")
    
    # Spinner karakterleri
    spinners = ["/", "-", "\\", "|"]
    current_spinner = spinners[a % 4]
    
    print(f"{Fore.YELLOW}[*] Checking System Files... {Fore.MAGENTA}{current_spinner} {Fore.WHITE}{a}/{len(file_list)}")
    
    time.sleep(0.05) # Hız biraz artırıldı
    check_files(file_list[:a])
    a += 1

os.system("cls" if os.name == "nt" else "clear")
draw_header()
msg(1, "Pars Bootloader 0.0.2")  
msg(1, "System Booting...")
print(f"{Fore.GREEN}[ OK ] Checking System Files... | {a-1}/{len(file_list)}!")
msg(3, "Loading kinetic...")

try:
    # Bu kısım sistem yoluna göre çalışır
    os.system("py /users/%USERNAME%/Desktop/Titanium/boot/kinetic.py" if os.name == "nt" else "/usr/bin/python3 /home/user/Titanium/boot/kinetic.py")
    msg(3, "Success!")
except Exception as e:
    msg(2, f"rootfs loading failed: {e}")
    exit(1)