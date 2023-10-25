from tkinter import Tk
from window import MainWindow
from LWindow import LW

if __name__ == "__main__":
    root = Tk()
    app = LW(root)
    root.mainloop()