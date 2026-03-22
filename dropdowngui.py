import tkinter as tk
root = tk.Tk()
opsi = tk.StringVar(value="A")
tk.OptionMenu(root, opsi, "A", "B", "C").pack()
root.mainloop()
