import os
import shutil
from colorama import Fore, Style
class MemMan:
    def __init__(self, username):
        self.username = username
        # Ana dizin yapısını belirle
        print("[",Fore.BLUE + "==============MemMan==============" + Fore.RESET)
        print("[",Fore.BLUE + "INFO" + Fore.RESET + "]",Fore.YELLOW + "MemMan v1 started..." + Fore.RESET)
        self.base_path = os.path.join(os.getcwd(), "..", "space", "user", self.username)
        self._initialize_storage()
        

    def _initialize_storage(self):
        """Kullanıcıya özel klasör yapısını diskte oluşturur."""
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            print("[",Fore.BLUE + "MemMan" + Fore.RESET + "]",Fore.YELLOW + f"Creating user space for: {self.username}..." + Fore.RESET)
        else:
            print("[",Fore.BLUE + "MemMan" + Fore.RESET + "]",Fore.YELLOW + f"System ready for: {self.username}" + Fore.RESET)

    def create_folder(self, folder_name):
        """Kullanıcı dizini içinde yeni bir klasör açar."""
        path = os.path.join(self.base_path, folder_name)
        try:
            os.makedirs(path, exist_ok=True)
            return f"Directory created: {folder_name}"
        except Exception as e:
            return f"Error: {e}"

    def write_file(self, filename, content):
        """Kullanıcı dizini içine dosya yazar/oluşturur."""
        path = os.path.join(self.base_path, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File saved: {filename}"

    def list_content(self, sub_dir=""):
        """Dizini listeler."""
        target = os.path.join(self.base_path, sub_dir)
        if os.path.exists(target):
            return os.listdir(target)
        return "Path not found."

    def delete(self, name):
        """Dosya veya klasörü siler."""
        path = os.path.join(self.base_path, name)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        return f"Deleted: {name}"

# --- Koşturma Bölümü (Örnek) ---
# if __name__ == "__main__":
#     # Kullanıcı adını sistemden veya inputla alabilirsin
#     user = input("Sisteme giriş yapacak kullanıcı adı: ")
#     fs = MemMan(user)

#     # Örnek işlemler
#     print(fs.create_folder("Documents"))
#     print(fs.write_file("Documents/selam.txt", "Bu dosya MemMan tarafından oluşturuldu."))
#     print(f"Mevcut dosyaların: {fs.list_content('Documents')}")