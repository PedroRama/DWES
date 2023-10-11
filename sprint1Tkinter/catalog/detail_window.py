import tkinter as tk
from tkinter import ttk

class Detail_window(cell):

    root = tk.Toplevel()

    root.title("Información sobre los peces")

    label = ttk.Label(root, image = cell.imagenLista)
    label.pack()
    label1 = ttk.Label(root, text = cell.title)
    label1.pack()
    label2 = ttk.Label(root, text = cell.description)
    label2.pack()

    root.mainloop()

        




