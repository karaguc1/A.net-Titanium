import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import os
import subprocess

def insert_node(tree, parent, path):
    node = tree.insert(parent, 'end', text=path, open=False)
    if os.path.isdir(path):
        tree.insert(node, 'end')

def open_folder(event):
    item = tree.selection()[0]
    path = tree.item(item, "text")
    if os.path.isdir(path):
        tree.delete(*tree.get_children(item))
        for filename in os.listdir(path):
            fullpath = os.path.join(path, filename)
            insert_node(tree, item, fullpath)

def open_file():
    item = tree.selection()[0]
    path = tree.item(item, "text")
    if os.path.isfile(path):
        subprocess.Popen(["xdg-open", path])

def new_file():
    item = tree.selection()[0]
    path = tree.item(item, "text")
    if not os.path.isdir(path):
        path = os.path.dirname(path)
    filename = simpledialog.askstring("Yeni Dosya", "Dosya adı:")
    if filename:
        fullpath = os.path.join(path, filename)
        with open(fullpath, "w") as f:
            f.write("")
        refresh_tree(item)

def new_folder():
    item = tree.selection()[0]
    path = tree.item(item, "text")
    if not os.path.isdir(path):
        path = os.path.dirname(path)
    foldername = simpledialog.askstring("Yeni Klasör", "Klasör adı:")
    if foldername:
        os.makedirs(os.path.join(path, foldername), exist_ok=True)
        refresh_tree(item)

def show_properties():
    item = tree.selection()[0]
    path = tree.item(item, "text")
    info = f"Path: {path}\n"
    if os.path.isdir(path):
        info += "Type: Folder\n"
    else:
        info += "Type: File\n"
        info += f"Size: {os.path.getsize(path)} bayt\n"
    messagebox.showinfo("Properties", info)

def refresh_tree(item):
    path = tree.item(item, "text")
    if os.path.isdir(path):
        tree.delete(*tree.get_children(item))
        for filename in os.listdir(path):
            fullpath = os.path.join(path, filename)
            insert_node(tree, item, fullpath)

def right_click(event):
    iid = tree.identify_row(event.y)
    if iid:
        tree.selection_set(iid)
        menu.tk_popup(event.x_root, event.y_root)

# Pencere oluştur
p = tk.Tk()
p.title("Bozkurt File Manager")
p.geometry("800x600")

# Treeview
tree = ttk.Treeview(p)
tree.pack(fill="both", expand=True)
tree.heading("#0", text="File Path", anchor='w')

# Sağ tıklama menüsü
menu = tk.Menu(p, tearoff=0)
menu.add_command(label="Open", command=open_file)
menu.add_command(label="New File", command=new_file)
menu.add_command(label="New Folder", command=new_folder)
menu.add_separator()
menu.add_command(label="Properties", command=show_properties)

# Başlangıç dizini
insert_node(tree, '', os.path.expanduser("~"))

# Eventler
tree.bind("<Double-1>", open_folder)
tree.bind("<Button-3>", right_click)

p.mainloop()
