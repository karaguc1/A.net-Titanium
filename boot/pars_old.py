import os
import subprocess
w=0
from time import *
import os
import time
import colorama
#import garsaun

colorama.init()
w=0
# Dosya listesi (aynı klasörde aranacak)
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
    # missing_files bir liste veya tek bir dosya olabilir
    if isinstance(missing_files, (list, tuple)):
        missing_display = ', '.join(f'"{f}"' for f in missing_files)
        path_display = ','.join(missing_files)
    else:
        missing_display = f'"{missing_files}"'
        path_display = missing_files

    error_msg = rf"""
 [!] CRITICAL SYSTEM ERROR: KERNEL_THREAD_NOT_HANDLED
 ----------------------------------------------------
 [ TIME ] {time.strftime("%Y/%m/%d %H:%M")}
 [ MODULE ] VFS_MOUNT_ROOT
 [ ERROR ] MISSING: {missing_display}
   _________________________________________
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

 PANIC: Unable to mount root fs on unknown-block(0,0)
 please visit www.a.com/anet/errors/0xE344240404 .
 ----------------------------------------------------
    """
    print(error_msg)


# Kontrol mekanizması: her dosyayı tek tek kontrol et
def check_files(files):
    base_dir = os.path.dirname(__file__) or os.getcwd()
    missing = []
    for f in files:
        path = os.path.join(base_dir, f)
        if not os.path.exists(path):
            missing.append(f)

    if missing:
        kernel_panic(missing)
        # Sistem kritik durumda, sonlandır
        exit(1)
    # else:
    #     # Tüm dosyalar mevcut
    #     print("[ OK ] Tüm gerekli dosyalar bulundu.")
sertificate=[".{00010001011110111001101001}@pard.{11101110100001000110010110}@pard.{01100110100100101000100001}@pard.{01110100000111101001111101}@pard?(11111111111111111111111111)@end![00000000000000000000000000]@endp"]
os.system("cls" if os.name == "nt" else "clear")
print(colorama.Back.WHITE + colorama.Fore.BLACK + "Welcome To Pars!" + colorama.Style.RESET_ALL)
sleep(2)
os.system("cls")
print("_"*40 , "\n")
print(" "*10,"A.net beta 0.0.5")
print("_"*40)
#from debug:print(sertificate)
def msg(tur,met):
    if tur == 1:
        print(f"[ INFO ]{met}")
    elif tur == 2:
        print(f"[ ERROR ]{met}")   
    elif tur == 3:
        print(f"[ OK ]{met}")
sleep(3)        
msg(1,"Pars Bootloader 0.0.2")  
sleep(2)      
msg(1,"System Booting...")
sleep(3)  
a=0
print(rf"[*] Checking System Files.../ {a}/{len(file_list)}")
while a<len(file_list)+1:
    print("_"*40 , "\n")
    print(" "*10,"A.net beta 0.0.5")
    print("_"*40)
    msg(1,"Pars Bootloader 0.0.2")  
    msg(1,"System Booting...")
    print(rf"[*] Checking System Files.../ {a}/{len(file_list)}")
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")
    print("_"*40 , "\n")
    print(" "*10,"A.net beta 0.0.5")
    print("_"*40)
    msg(1,"Pars Bootloader 0.0.2")  
    msg(1,"System Booting...")
    print(rf"[*] Checking System Files...- {a}/{len(file_list)}")
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")
    print("_"*40 , "\n")
    print(" "*10,"A.net beta 0.0.5")
    print("_"*40)
    msg(1,"Pars Bootloader 0.0.2")  
    msg(1,"System Booting...")
    print(rf"[*] Checking System Files...\ {a}/{len(file_list)}")
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")
    print("_"*40 , "\n")
    print(" "*10,"A.net beta 0.0.5")
    print("_"*40)
    msg(1,"Pars Bootloader 0.0.2")  
    msg(1,"System Booting...")
    print(rf"[*] Checking System Files...| {a}/{len(file_list)}")
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")
    check_files(file_list[:a])
    a += 1
os.system("cls" if os.name == "nt" else "clear")
print("_"*40 , "\n")
print(" "*10,"A.net beta 0.0.5")
print("_"*40)
msg(1,"Pars Bootloader 0.0.2")  
msg(1,"System Booting...")
print(rf"[ OK ] Checking System Files...| {a-1}/{len(file_list)}!")
msg(3,"Loading kinetic...")
try:
    os.system("py /users/%USERNAME%/Desktop/Titanium/boot/kinetic.py" if os.name == "nt" else "/usr/bin/python3 /home/user/Titanium/boot/kinetic.py")
    msg(3,"Success!")
except Exception as e:
    msg(2,f"rootfs loading failed: {e}")
    exit(1)
# sleep(3)
# msg(1,"Loading system files...")
# while w<1025:
#     #print("_"*40 , "\n")
# 	#print(" "*10,"A.net beta 0.0.5")
# 	#print("_"*40)
#     #msg(1,"Pars Bootloader 0.0.2")
#     #msg(1,"System Booting...")
#     #msg(1,"Loading kernel...")
#     #msg(3,"Success!")
#     #msg(1,"Loading system files...")
#     msg(3,f"'{w}'  files loaded! ")
#     sleep(0.0000001)
#     #os.system("clear") 
#     w=w+1
# msg(1,"Gui Service Starting...")
# sleep(2)
# msg(3,"Sucsess!")
# sleep(3)
# msg(1,"Switching to Gui...")
# sleep(5)
# msg(3,"Sucsess!")
# sleep(2)
# msg(3,"Bootloading ended!")
# os.system("/usr/bin/python3 /home/user/kernel/giris.py")
