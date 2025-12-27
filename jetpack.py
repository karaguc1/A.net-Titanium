import os
import zipfile
import shutil
import subprocess
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def jetpack_engine(pack_name):
    """
    Bu fonksiyon bir .aupac dosyasını gerçek bir uygulama gibi kurar.
    """
    # Paket yolu (İndirilenler klasöründe olduğunu varsayıyoruz)
    pack_path = os.path.join(BASE_DIR, "repository", pack_name)
    
    if not os.path.exists(pack_path):
        print(f"HATA: {pack_name} bulunamadı.")
        return False

    try:
        # 1. Paketi geçici bir klasöre aç
        temp_dir = os.path.join(BASE_DIR, "temp_install")
        if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        with zipfile.ZipFile(pack_path, 'r') as aupac:
            aupac.extractall(temp_dir)

        # 2. Kurulum Talimatlarını Oku (manifest.txt varsa)
        # Eğer paket bir sistem güncellemesi ise (kernel dosyası içeriyorsa)
        if "kernel" in pack_name.lower():
            return apply_system_update(temp_dir)
        
        # 3. Uygulamayı 'apps' klasörüne taşı
        app_folder_name = pack_name.replace(".aupac", "")
        final_dest = os.path.join(BASE_DIR, "apps", app_folder_name)
        
        if os.path.exists(final_dest): shutil.rmtree(final_dest)
        shutil.move(temp_dir, final_dest)

        # 4. Varsa bağımlılıkları yükle (pip install gibi)
        requirements = os.path.join(final_dest, "requirements.txt")
        if os.path.exists(requirements):
            subprocess.run(["pip", "install", "-r", requirements])

        print(f"[*] {app_folder_name} başarıyla kuruldu.")
        return True

    except Exception as e:
        print(f"KRİTİK HATA: {e}")
        return False

def apply_system_update(update_path):
    """Sistemi (kernel, desk, vb.) güncelleyen hassas fonksiyon."""
    try:
        # Gelen paketteki tüm dosyaları ana dizine (BASE_DIR) kopyala (üzerine yazar)
        for item in os.listdir(update_path):
            s = os.path.join(update_path, item)
            d = os.path.join(BASE_DIR, item)
            if os.path.isdir(s):
                if os.path.exists(d): shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        print("[+] Sistem dosyaları güncellendi.")
        return True
    except:
        return False