import tkinter as tk
root = tk.Tk()
lb = tk.Listbox(root)
for i in ["A","B","C"]:
    lb.insert(tk.END, i)
lb.pack()
root.mainloop()
