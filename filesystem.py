import os
import shutil
import datetime
import akrl # Renkli çıktılar için
import diskmanager as dm # Temel disk işlemleri için

class FileSystem:
    def __init__(self):
        # A.net sisteminin kök dizini
        self.root_path = "/home/user/kernel"
        self.apps_path = os.path.join(self.root_path, "apps")
        self.sys_path = os.path.join(self.root_path, "set")

    def list_dir(self, path="."):
        """Dizini listeler ve dosya/klasör ayrımı yapar."""
        try:
            files = os.listdir(path)
            print(f"\n{'AD':<20} {'TÜR':<10} {'BOYUT':<10}")
            print("-" * 40)
            for f in files:
                full_path = os.path.join(path, f)
                ftype = "KLASÖR" if os.path.isdir(full_path) else "DOSYA"
                size = os.path.getsize(full_path)
                print(f"{f:<20} {ftype:<10} {size:<10} bytes")
        except Exception as e:
            akrl.red(f"Hata: {e}")

    def create_vdisk(self, name, size_mb):
        """Sanal bir disk alanı (img) oluşturur."""
        path = os.path.join(self.root_path, f"{name}.vdisk")
        try:
            with open(path, "wb") as f:
                f.write(b'\0' * (size_mb * 1024 * 1024))
            akrl.green(f"[+] {size_mb}MB boyutunda sanal disk oluşturuldu: {name}")
        except Exception as e:
            akrl.red(f"Disk oluşturma hatası: {e}")

    def secure_delete(self, path):
        """Dosyayı diskmanager kullanarak geri döndürülemez siler."""
        if os.path.exists(path):
            akrl.yellow(f"[*] {path} güvenli şekilde siliniyor...")
            dm.sdy(path) # diskmanager içindeki güvenli silme fonksiyonu
        else:
            akrl.red("Dosya bulunamadı.")

    def get_stats(self):
        """Sistem depolama bilgilerini verir."""
        usage = shutil.disk_usage(self.root_path)
        akrl.cyan(f"--- SİSTEM DEPOLAMA DURUMU ---")
        print(f"Toplam: {usage.total / (1024**3):.22f} GB")
        print(f"Kullanılan: {usage.used / (1024**3):.22f} GB")
        print(f"Boş: {usage.free / (1024**3):.22f} GB")

    def check_integrity(self, file_list):
        """Sistem dosyalarının yerinde olup olmadığını kontrol eder (Pars mantığı)."""
        missing = []
        for f in file_list:
            if not os.path.exists(os.path.join(self.root_path, f)):
                missing.append(f)
        return missing

# Test Kullanımı
if __name__ == "__main__":
    fs = FileSystem()
    fs.get_stats()
    fs.list_dir()