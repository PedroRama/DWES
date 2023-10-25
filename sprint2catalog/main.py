from tkinter import Tk
from window import MainWindow
from LWindow import LW
import threading

if __name__ == "__main__":
    root = Tk()
    app = LW(root)
    root.mainloop()