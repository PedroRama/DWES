import json
import threading
import tkinter as tk
import requests
from window import MainWindow

class LW:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando..")
        self.root.geometry("170x120")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg")##color

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0##inicializamos atributo a 0

        self.draw_progress_circle(
            self.progress)

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        self.check_thread()

        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")

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

    def fetch_json_data(self):
        response = requests.get("https://api.github.com/repos/PedroRama/DWES/contents/catalog.json?ref=main") ##archivo json
        if response.status_code == 200:
            json_data = response.json()  ##Respuesta variable json
            self.finished=True

    def check_thread(self):
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

    def launch_main_window(json_data):
        root = tk.Tk()
        app = MainWindow(root, json_data)
        root.mainloop()
