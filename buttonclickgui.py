import tkinter as tk
def klik():
    print("Diklik!")
root = tk.Tk()
tk.Button(root, text="Klik", command=klik).pack()
root.mainloop()
