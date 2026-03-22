import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Fungsi untuk membuat file baru
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

# Fungsi untuk membuka file
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
            root.title(f"{os.path.basename(file_path)} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka file: {e}")

# Fungsi untuk menyimpan file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"{os.path.basename(file_path)} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

# Membuat area teks
text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill="both")

# Scrollbar
scroll_bar = tk.Scrollbar(text_area)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=text_area.yview)

# Menu bar
menu_bar = tk.Menu(root)

# Menu File
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Menu Edit
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", command=text_area.edit_redo)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Menambahkan menu ke jendela
root.config(menu=menu_bar)

# Menjalankan aplikasi
root.mainloop()