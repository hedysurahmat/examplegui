import tkinter as tk
def pilih():
    print(var.get())
root = tk.Tk()
var = tk.StringVar()
tk.Radiobutton(root, text="A", variable=var, value="A", command=pilih).pack()
tk.Radiobutton(root, text="B", variable=var, value="B", command=pilih).pack()
root.mainloop()
