
import diskmanager as dm
import os
import time
import datetime
#import psutil
import shutil
import akrl
import coremath as cm
import opengui as og
def init():
    def r():
        return init()
    ver="merve"
    user="Anet-user1"
    password="acomranet1453"
    yol="M:/anet/komutcekirdegi/ana"
    i=input(f"arminal$#konsole & A.net?{ver} | {yol} @!kök>")
    if i=="netver":
        print("A.net merve 0.0.2")
        r()
    elif i=="sil":
        os.system("clear")
        r()
    elif i=="temizle":
        os.system("clear")
        r()
    elif i=="":
        None
        r()
    elif i=="çık":
        exit(1)
    elif i.startswith("yazdır "):
        s=i[6:]
        print(s)
        r()
    elif i=="a.net?sürpriz//pttis1453&fetih1071":
        print("bu bir sürpriz yumurta!\ntebrikler yumurtavcısı!\nseni seviyorum merve(kuzenim)!!!\nseni seviyorum mustafa(kuzenim) NOT:sen çok havalısın!(maşaAllah:))\ni very love you beyza (aunt) becuase you are very great!:)")
        r()
    elif i=="gücü kapat":
        os.system("sudo poweroff")
        r()
    elif i=="çıkış yap":
        os.system("pkill -KILL -u  $USER")
        r()
    elif i=="yeniden aç":
        os.system("sudo reboot")
        r()
    elif i=="bilgi-al(zaman)":
       print(datetime.datetime.now())
       r()
    elif i=="hata-ayıklama-kod(2013)":
        akrl.red("[                                                  [0%]                                                    ]")
        akrl.yellow("[################################################# [50%]                                                  ]")
        akrl.green("[##################################################[100%]##################################################]")
        r()
    elif i=="servis başlat":
        s=input("servis adı:")
        dm.ac(f"{s}.servis")
        r()
    elif i=="yeni dosya":
        n=input("dosya adı:")
        dm.do(n)
        r()
    elif i=="dosya sil":
        n=input("dosya adı:")
        dm.ds(n)
        r()
    # elif i=="jetpack":
    #     dm.ac("jetpack.exe")
    #     exit(1)
    elif i=="jetpack":
        os.system("python jetpack.py")
        r()
    elif i=="kök":
        def root():
            p=input(f"[kök]şunu söylüyor: '{user} için şifre':")
            if p==password:
                os.system("python r.arminal.py")
                exit(1)
            else:
                print("Affedersin,lütfen tekrar dene.")
                r()
        root()
    elif i=="yardım":
        print("çık\nyazdır <ÇIKTI>\ngücü kapat\nçıkış yap\nyeni dosya\ndosya sil\nyardım\nservis başlat\nbilgi-al(time)\njetpack\nyeniden aç.")
        r()
    elif i=="ls":
        os.system(i)
        r()
    elif i=="ağaç":
        os.system("tree")
        r()
    else:
        print(f"'{i}' erişilemez veya çalıştırılamaz.")
        r()
if __name__=="__main__":
    init()
