import diskmanager as dm
import os
import time
import datetime
import psutil
import shutil
from colorama import *
# import coremath as cm
# import opengui as og
def main():
	print(Fore.CYAN + "=================anet kernel-v05-a8d9fvw99382============" + Fore.RESET)
	print("[",Fore.BLUE + "INFO" + Fore.RESET + "]",Fore.YELLOW + "logging activity..." + Fore.RESET)
	def alog():
		dosya_adi = "kernel.log"
		logdate = datetime.datetime.now()
		disk_usage = psutil.disk_usage('/')
	
		if os.path.isfile(dosya_adi):
			def klog(value):
				dm.yaz("kernel.log",f"{value}")
			def kloge(value):
				dm.uyaz("kernel.log",f"\n{value}")
			disk_usage = shutil.disk_usage("/")  # Disk bilgilerini al
			disk_total_gb = disk_usage.total / (1024 ** 3)
			kloge(f"_________________________________________________________\nS:tarih {logdate}\nS:Çekirdek Başarıyla Yüklendi!\nS:Depolama Tespit Ediliyor...\nS:{disk_total_gb:.2f} GB Depolama tespit edildi!")
			# klog("S:date {logdate}\nS: Kernel Loaded Succsesfully\nS:Detecting Memory...\nS:{:.2f} GB Disk Detected!".format(disk_usage.total / (1024 ** 3)))
			kloge("S:Klavye Test Ediliyor...\n0123456789abcçdefgğhıijklmnoöprsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVWXYZ<>£#$½{}[]!'^+%&/()=?*-_")
		else:
			dm.do(dosya_adi)
			def klog(value):
				dm.yaz("kernel.log",f"{value}")
			def kloge(value):
				dm.uyaz("kernel.log",f"\n{value}")
			disk_usage = shutil.disk_usage("/")  # Disk bilgilerini al
			disk_total_gb = disk_usage.total / (1024 ** 3)
			kloge(f"_________________________________________________________\nS:tarih {logdate}\nS:Çekirdek Başarıyla Yüklendi!\nS:Depolama Tespit Ediliyor...\nS:{disk_total_gb:.2f} GB Depolama tespit edildi!")
			# klog("S:date {logdate}\nS: Kernel Loaded Succsesfully\nS:Detecting Memory...\nS:{:.2f} GB Disk Detected!".format(disk_usage.total / (1024 ** 3)))
			kloge("S:Klavye Test Ediliyor...\n0123456789abcçdefgğhıijklmnoöprsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVWXYZ<>£#$½{}[]!'^+%&/()=?*-_")
	def kloge(value):
				dm.uyaz("kernel.log",f"\n{value}")
	alog()
	# dm.ref()
	print("[",Fore.GREEN + "OK" + Fore.RESET + "]",Fore.YELLOW + "activity logged successfully!" + Fore.RESET)
	print("[",Fore.BLUE + "INFO" + Fore.RESET + "]",Fore.YELLOW + "starting metaui..." + Fore.RESET)

	os.system("py /users/%USERNAME%/Desktop/Titanium/giris.py &" if os.name == 'nt' else "/usr/bin/python3 /home/user/Titanium/giris.py &")


	while True:
		pass
		



	#işte bilgisayardaki disk algılama kodları falan

if __name__ == '__main__':
	main()