import diskmanager as dm
import os
import time
import datetime
import psutil
import shutil
import coremath as cm
import opengui as og
def init():
    time=datetime.datetime.now()
    def r():
        return init()
    ver="classic"
    path="M:/anet/commandcore/main"
    i=input(f"jetpack$#console & A.net?{ver} | {path} @root>")
    if i=="?v?":
        print("jetpack v0.0.1")
        r()
    elif i=="cls":
        os.system("cls")
        r()
    elif i=="clear":
        os.system("cls")
        r()
    elif i=="":
        None
        r()
    elif i=="exit":
        exit(1)
    # elif i==f"echo ":
    #     s=i[4:]
    #     print(s)
    elif i=="a.net?easter//pttis1453&fetih1071":
        print("this is an easter egg!\nIO EGGHAUNTER!\ni love you merve(cousin)!!!\ni love you mustafa(cousin) NOTE:you are very cool!(mashaAllah:))\ni very love you beyza (aunt) becuase you are very great!:)")
        r()
    elif i=="arminal":
        dm.ac("arminal.exe")
        exit(1)
    elif i=="jetpack depack":
        g=input("package name:")
        with open(f"{g}.anetupdatepackage","r") as pack:
            pack1=pack.read()
            with open("set/update.set","a") as up:
                up.write(pack1)
                r()
    else:
        print(f"'{i}' is inacsessable or not executable this platform.")
        r()
if __name__=="__main__":
    init()