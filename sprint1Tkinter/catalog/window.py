from tkinter import ttk
import tkinter as tk
from cell import Cell
from detail_window import Detail_window

class MainWindow():

    def on_button_click(self, cell):
        Detail_window(cell)

    def __init__(self, root):
        root.title("Peces_Acuario")

        self.cells = [
            Cell("PEZ1", "C:\\Users\\pedro\\Desktop\\sprint1Tkinter\\catalog\\data\\unedited\\disco.jpg", "El pez disco es un género de pez de la familia de los cíclidos. Es originario de las zonas bajas del río Amazonas y sus afluentes, pertenece a la familia de los cíclidos de origen sudamericano. "),
            Cell("PEZ2", "C:\\Users\\pedro\\Desktop\\sprint1Tkinter\\catalog\\data\\unedited\\angel.jpg", "El escalar,  o pez angel es uno de los reyes de nuestros acuarios. Es de esos peces que atraen todas las miradas en un acuario por su elegancia y su tan característica forma."),
            Cell("PEZ3", "C:\\Users\\pedro\\Desktop\\sprint1Tkinter\\catalog\\data\\unedited\\beta.jpg", "El pez betta o luchador de Siam (Betta splendens) es una especie de pez de agua dulce de la familia de los osfronémidos en el orden de los Perciformes."),
            Cell("PEZ4", "C:\\Users\\pedro\\Desktop\\sprint1Tkinter\\catalog\\data\\unedited\\neon.jpg", "El Paracheidoron Inessi o tetra neón es un pequeño pez tropical de agua dulce que procede de América del Sur."),
            Cell("PEZ5", "C:\\Users\\pedro\\Desktop\\sprint1Tkinter\\catalog\\data\\unedited\\caracol.jpg", "CARACOL ANENTOME HELENA (ASESINO). Conocido como caracol asesino porque se alimenta de otros caracoles, es ideal para acabar con las plagas y mantenerlas controladas.")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.imagenLista, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_click(cell))
