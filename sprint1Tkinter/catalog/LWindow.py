import json
import threading
import tkinter as tk

##en las líneas superiores importamos lo necesario

class LW:
    def __init__(self, root):
        self.root = root ##ventana carga
        self.root.title("Cargando..") ## Titulo de la ventana
        self.root.geometry("170x120") ## Tamaño de la ventana
        self.root.resizable(False, False) ## No podrá variar el tamaño de la ventana

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14)) ##tamaño y tipo e letra
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")##color

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0##inicializamos atributo a 0

        self.draw_progress_circle(self.progress) ## pasarmeos a la funciona el atributo con valor 0, en este caso "self.preogress"

        self.update_progress_circle()


    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")  #Linea para boorrar dibuos anteriores al "lanzamiento".
        angle = int(360 * (progress/100))

        self.canvas.create_arc(10, 10, 35, 35,
                               start=0, extent=angle, tags="progress", outline='red', width=4, style=tk.ARC)


    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 7
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)