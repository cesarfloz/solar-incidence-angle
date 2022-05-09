import tkinter as tk
from tkinter import * 
from PIL import ImageTk , Image
from tkinter import messagebox


class AnguloInSolar(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.txt_fahrenheit = tk.Entry(self.master, width=10)
        self.txt_fahrenheit.grid(row=0, column=0, sticky='e', padx=10, pady=10)

        lbl_fahrenheit = tk.Label(self.master, text="\N{DEGREE FAHRENHEIT}")
        lbl_fahrenheit.grid(row=0, column=1, sticky='w', padx=10, pady=10)

        btn_convertir = tk.Button(self.master, text='Obtener angulo', command=self.convertir)
        btn_convertir.grid(row=0, column=2, padx=10, pady=10)

        self.lbl_celsius = tk.Label(self.master, text='\N{DEGREE CELSIUS}')
        self.lbl_celsius.grid(row=0, column=3, padx=10, pady=10)
    
    def convertir(self):
        try:
            fahrenheit = float(self.txt_fahrenheit.get())

            celsius = (5/9) * (fahrenheit - 32)

            self.lbl_celsius['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'
        except:
            messagebox.showwarning('Error', 'Debe escribir un número (float) en los campos.')

def main():
    root = tk.Tk()
    root.geometry("450x350")
    root.title("Angulo de incidencia solar")
    #window.iconbitmap("img/logo.png")
    root.resizable(0,0)

    image = Image.open("img/logo.png")
    image = image.resize((90,80), Image.ANTIALIAS)
    imagen = ImageTk.PhotoImage(image)
    Label(root,image=imagen).place(x=357,y=265)

    window = AnguloInSolar(root)
    window.mainloop()

if __name__ == "__main__":
    main()