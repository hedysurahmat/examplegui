import tkinter as tk
root = tk.Tk()
text = tk.Text(root)
text.pack()
def simpan():
    with open("note.txt","w") as f:
        f.write(text.get("1.0", tk.END))
tk.Button(root, text="Simpan", command=simpan).pack()
root.mainloop()
