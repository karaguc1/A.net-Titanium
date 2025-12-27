import os
import time
import akrl
def permissionerror():
    akrl.red("HATA:Erişim Engellendi.")

def sdy(value):
    i=input("bu işlem diskinizdeki silinmiş verileri GERİ GETİRMESİ İMKANSIZ ŞEKİLDE SİLECEKTİR!(Devam etmek istediğinizden emin iseniz evet yazın)...\n")
    if i == "evet":
        try:
            
            os.system(f"cipher /w:{value}")
        except PermissionError:
            permissionerror()
    else:
        None
def do(value):
    try:
        open(f"{value}","x")
    except FileExistsError:
        akrl.red("HATA: Dosya zaten var.")
    except PermissionError:
        permissionerror()
def oku(value):
    try:
        with open(f"{value}","r") as f:
            f1=f.read()
            print(f"dosya içeriği:\n{f1}")
    except FileNotFoundError:
        akrl.red("HATA: Dosya bulunamadı.")
    except PermissionError:
        permissionerror()
def ko(value):
    try:
        os.system(f"md {value}")
    except PermissionError:
        permissionerror()
def ds(value):
    try:
        os.remove(f"{value}")
    except FileNotFoundError:
        akrl.red("HATA:Dosya bulunamadı.")
    except PermissionError:
        permissionerror()
def ks(value):
    try:
        os.removedirs(f"{value}")
    except FileNotFoundError:
        akrl.red("HATA:Klasör bulunamadı.")
    except PermissionError:
        permissionerror()

def yaz(value,value1):
    try:
        with open(f"{value}","w") as f:
            f.write(f"{value1}")
    except FileNotFoundError:
        # akrl.red("HATA:Dosya bulunamadı.")
        None
    except PermissionError:
        permissionerror()
def uyaz(value,value1):
    try:
        with open(f"{value}","a") as f:
            f.write(f"{value1}")
    except FileNotFoundError:
        # akrl.red("HATA:Dosya bulunamadı.")
        None
    except PermissionError:
        permissionerror()
# def ref():
#     yaz("set\gui.set","guistatus=deactive")
#     time.sleep(2)
#     yaz("set\gui.set","guistatus=active")
def ac(value):
    try:
        os.startfile(value)
    except FileNotFoundError:
        print("Hata:Dosya Bulunamadı.")
