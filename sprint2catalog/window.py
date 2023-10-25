from tkinter import Canvas, Frame, Label, Scrollbar, messagebox, ttk
import tkinter as tk

import requests
from cell import Cell
from detail_window import Detail_window
from PIL import Image, ImageTk
from io import BytesIO

class MainWindow():

    def load_image_from_url(self, url):
        response = requests.get(url)
        imagen_data = Image.open(BytesIO(response.content))
        imagen = ImageTk.PhotoImage(
            (imagen_data).resize((170, 120), Image.Resampling.LANCZOS))  ## Hacemos resize a la imagen
        return imagen

    def on_button_click(self, cell):
        Detail_window(cell)

    def on_button_clicked2(self):
        mensaje = "Proyecto realizado con python."
        messagebox.showinfo("Creador", mensaje)

    def __init__(self, root, json_data):
        root.title("5 peces:")

    def __init__(self, root, json_data):
        root.title("Top 5 Juegos:")
        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(root, orient="vertical",## Canvas para dibujar ventana principal.
                                   command=self.canvas.yview)##Crea Scrollbar.

        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>",
                                   lambda e: self.canvas.configure(
                                       scrollregion=self.canvas.bbox("all")
                                   ))
                                    ##reconfiguramos el lienzo en caso que se desconfigure

        self.canvas.create_window((0, 0), window=self.scrollable_frame,
                                  anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)## Configuraremos el lienzo.

        self.cell_list = []

        for item in json_data:
            n = item["name"]## Pasamos variable
            descripcion = item["descripcion"]
            url = item["image_url"]
            imagen = self.load_image_from_url(
                url)

            cell = Cell(n, descripcion, url,
                        imagen)
            self.cell_list.append(
                cell)

            self.canvas.grid(row=0, column=0, sticky="nsew")## En este paso pondremos el lienzo
            self.scrollbar.grid(row=0, column=1, sticky="ns")## En este paso pondremos la barra

            root.grid_rowconfigure(0, weight=1)
            root.grid_columnconfigure(0, weight=1)

            frame = Frame(self.scrollable_frame)## Marco del contenido a mostrar
            frame.pack(pady=10)

            label = Label(frame, image=cell.imagen, text=n, compound=tk.BOTTOM) ##mostramos imagen
            label.grid(row=0, column=0)

            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))

        x = (
                        root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)

        menu_archivo.add_command(label="Acerca de", command=self.on_button_clicked2)
        barra_menus.add_cascade(menu=menu_archivo, label="Ayuda")
        root.config(menu=barra_menus)


