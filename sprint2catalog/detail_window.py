import tkinter as tk
from tkinter import ttk


def Detail_window(cell):
    root = tk.Toplevel()

    root.title("Información extra acerca del juego.")  ## Título

    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f"+{int(x)}+{int(y)}")

    label1 = ttk.Label(root, text=cell.name)  ## Se guardará el titulo
    label1.pack()
    label = ttk.Label(root, image=cell.imagen,
                      compound=tk.BOTTOM)  ## Llamar foto almacenada en cell
    label.pack()
    label2 = ttk.Label(root, text=cell.descripcion)  ## Descripción
    label2.pack()

    root.mainloop()

        




