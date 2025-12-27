import os
import time

# Dosya listesi (aynı klasörde aranacak)
file_list = [
    "addu.py",
    "akrl.py",
    "arminal.py",
    "aver.py",
    "ayarlar.py",
    "connectornet.py",
    "control.py",
    "desk.py",
    "diskmanager.py",
    "fmngr.py",
    "giris.py",
    "hm.py",
    "jetpack.py",
    "kernel-v0.0.2.py",
    "mpp.py",
    "pars.py",
    "r.arminal.py",
    "rbt.py",
    "readme.txt",
    "root.jetpack.py",
    "shd.py",
    "webb.py",
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
  \\\_________________________________________/

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


# Program başlarken kontrolü çalıştır
if __name__ == '__main__':
    a=0
    while a<len(file_list)+1:
        print(rf"[*] Checking System Files.../ {a}/{len(file_list)}")
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")
        print(rf"[*] Checking System Files...- {a}/{len(file_list)}")
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")
        print(rf"[*] Checking System Files...\ {a}/{len(file_list)}")
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")
        print(rf"[*] Checking System Files...| {a}/{len(file_list)}")
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")
        check_files(file_list[:a])
        a += 1
    print(rf"[*] Checking System Files...| {a-1}/{len(file_list)}")
    print("[ OK ] All system files are present.")