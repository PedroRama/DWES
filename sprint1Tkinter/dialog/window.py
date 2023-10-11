from tkinter import ttk
from yes_window import Window_Y
from no_window import Window_N

class MainWindow():
   
    def __init__(self, root) -> None:
        self.root = root 

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(text="¿Quieres comprar peces peces?") 
        self.label.pack()

        self.button1 = ttk.Button(root, text="Si", command = Window_Y) 
        self.button1.pack(side="left")

        self.button2 = ttk.Button(self.frame, text="No", command = Window_N) 
        self.button2.pack(side="right")

    



