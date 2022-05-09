from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("450x350")
root.title("Angulo de incidencia solar")




clicked = StringVar()
options = [
    "Eafit route",
    "Darwin - Tennant Creek"
]
combo = ttk.ComboBox(root)
combo.current(0)

root.mainloop()