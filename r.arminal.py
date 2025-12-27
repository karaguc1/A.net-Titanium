import diskmanager as dm
import os
import time
import datetime
import psutil
import shutil
import akrl
import coremath as cm
import opengui as og
def init():
    def r():
        return init()
    ver="classic"
    user="Anet-user1"
    password="acomranet1453"
    path="M:/anet/mcsa/main"
    i=input(f"arminal$#console & A.net?{ver} | {path} @root>")
    if i=="netver":
        print("A.net classic 0.0.2")
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
    elif i=="power off":
        os.system("poweroff")
        r()
    elif i=="power out":
        os.system("pkill -KILL -u  $USER")
        r()
    elif i=="repower":
        os.system("reboot")
        r()
    elif i=="get-info(time)":
       print(datetime.datetime.now())
       r()
    elif i=="debug-code(2013)":
        akrl.red("[                                                  [0%]                                                    ]")
        akrl.yellow("[################################################# [50%]                                                  ]")
        akrl.green("[##################################################[100%]##################################################]")
        r()
    elif i=="start service":
        s=input("service name:")
        dm.ac(f"{s}.service")
        r()
    elif i=="newfile":
        n=input("filename:")
        dm.do(n)
        r()
    elif i=="delfile":
        n=input("filename:")
        dm.ds(n)
        r()
    elif i=="jetpack":
        dm.ac("jetpack.exe")
        exit(1)
    elif i=="root":
        def root():
            p=input(f"[root] password for '{user}':")
            if p==password:
                dm.ac("root.arminal.exe")
                exit(1)
            else:
                print("Sorry please try again.")
                r()
        root()
    elif i=="help":
        print("power off                            DESCRIPTION:shutdowns your computer.\npower out                        DESCRIPTION:goes log out.\nrepower                     DESCRIPTION:restarts your computer.\njetpack                     DESCRIPTION:starts jetpack application.\nnetver                     DESCRIPTION:print your a.net's version.\nnewfile                     DESCRIPTION:makes a file.\ndelfile                     DESCRIPTION:deletes a file.\nexit                     DESCRIPTION:goes exit\ncls/clear                     DESCRIPTION:clears this screen\nroot                     DESCRIPTION:makes you root\nget-info(time)                     DESCRIPTION:gives information about time\nhelped! 11 components listed succsessfully!")
        r()
    elif i=="ls":
        os.system(i)
        r()
    elif i=="tree":
        os.system(i)
        r()
    else:
        print(f"'{i}' is inacsessable or not executable.")
        r()
if __name__=="__main__":
    init()