import tkinter as tk
def tampil():
    label.config(text=entry.get())
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Tampil", command=tampil).pack()
label = tk.Label(root)
label.pack()
root.mainloop()
