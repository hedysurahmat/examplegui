import tkinter as tk
def hitung():
    hasil.config(text=int(e1.get()) + int(e2.get()))
root = tk.Tk()
e1 = tk.Entry(root); e1.pack()
e2 = tk.Entry(root); e2.pack()
tk.Button(root, text="+", command=hitung).pack()
hasil = tk.Label(root); hasil.pack()
root.mainloop()
