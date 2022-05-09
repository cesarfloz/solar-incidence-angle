
from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
import math


#############################################################################################################################
"""
Ventana
"""

# from app import main
class Ap:
    def __init__(self):
        self.beta = ""

ap = Ap()
window = Tk()
window.geometry("450x350")
window.title("Angulo de incidencia solar")
window.iconbitmap("img/logo.png")
window.resizable(0,0)

image = Image.open("img/logo.png")
image = image.resize((90,80), Image.ANTIALIAS)
imagen = ImageTk.PhotoImage(image)
Label(window,image=imagen).place(x=357,y=265)
# Creating a dropdown menu.

texto = StringVar()
combo = ttk.Combobox(window)
combo.place(x=60, y=90)
combo['values'] = ['Eafit route', 'Darwin - Tennant Creek']
combo.current(0)

# def switchButtonState():
#     if (btn1['state'] == tk.NORMAL):
#         btn1.config(state=tk.DISABLED)
#     else:
#         print("Error")



Label(text="Ingrese los parametros : ",fg="#F4FEFF", bg="darkblue", width="300", height="2" ,font=("Corbel 17")).pack()
sellec = Label(text="Selecciona la ruta a calcular:").place(x=60, y=110).pack()
sellec.place(x=60, y=110)
Label(text="").pack()
Label(text="").pack()

Label(text="Ingrea el angulo beta (°):").pack()
beta=Entry(window, width=36).pack()
Label(text="").pack()

Label(text="Ingrea algo:").pack()
algo=Entry(window, width=36).pack()
Label(text="").pack()

# Label(text="Ingrea otra cosa:").pack()
# entru1=Entry(window, width=36).pack()
# Label(text="").pack()

print(algo)

#############################################################################################################################

def angle():

    eafit_route={
    (-75.57961649782575,6.199852771569621), (-75.57982785231248,6.199011827680376),
    (-75.57999108538824,6.198426515756492), (-75.58038157884144,6.197326220433411),
    (-75.58066319682717,6.196590859536479), (-75.58100948447769,6.195550828599088)}

    # q = 19874 #J
    # t = 3600 #seconds
    # s = 5 # cm**2
    # e = 800 #W/m**2
    # """
    # El angulo formado por la superficie es de 90-angulo con la horizontal
    # """
    # #flujo_de_radiaccion_luminosa = e*s*math.cos()

    # flujo_radiante = q/t 

    # cos_de_alfa = q/(e*s*t)
    # print(cos_de_alfa)
    # #0.0013801388888888889
    # angulo =math.acos(0.0013801388888888889)
    # print(angulo)
    # #1.5694161874678632 rad
    # resultado_grados = angulo*(180/math.pi)
    # print(f"Resultado en grados: {resultado_grados}")



    longitud = -75.57961649782575



    # angulo de declinacion = 23,45
    s = 23.45

    #la = float(input("Ingrese el valor de La: "))
    la = 6.199852771569621  #Latitud



    vel=1200*9.8*math.sin(18)*85
    print(vel)

    b = beta.get()


    dia_del_año=110
    y = ((2*math.pi)/365)*((dia_del_año-1)+((12-12)/24))
    # y = float(input("Ingrese el valor de y: "))

    # dia_del_año=110
    # y = ((2*math.pi)/365)*((dia_del_año-1)+((12-12)/24))
    # print(y)

    w=algo.get()

    #w = angulo hora de la placa  -180.36°
    # w = float(input("Ingrese el valor de w: "))

    cos =((math.sin(s)*math.sin(la)*math.cos(b)) -
    (math.sin(s)*math.cos(la)*math.sin(b)*math.cos(y)) + 
    (math.cos(s)*math.cos(la)*math.cos(b)*math.cos(w)) + 
    (math.sin(s)*math.sin(la)*math.sin(b)*math.cos(y)*math.cos(w)) + 
    (math.cos(s)*math.sin(b)*math.sin(y)*math.sin(w)))

    print(cos)
    resultado_angulo_rad = math.acos(cos)
    print(f"Resultado en radianes: {resultado_angulo_rad}")
    resultado_grados = resultado_angulo_rad*(180/math.pi)
    print(f"Resultado en grados: {resultado_grados}")

Button(window, text = "Ejecutar",height="2", width="30",bg="gray", command=lambda:angle).pack() 

window.mainloop()