import tkinter as tk
def cek():
    print(var.get())
root = tk.Tk()
var = tk.IntVar()
tk.Checkbutton(root, text="Pilih", variable=var, command=cek).pack()
root.mainloop()
