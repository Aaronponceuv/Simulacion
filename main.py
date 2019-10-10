import tkinter as tk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt
from time import time

from Distribuciones.Exponencial import Exponencial
from Distribuciones.Erlang import Erlang
from Distribuciones.Normal import Normal
from Distribuciones.UnifomeContinua import UnifomeContinua
from Distribuciones.Binomial import Binomial
from Distribuciones.Poisson import Poisson
from Distribuciones.Geometrica import Geometrica
from Distribuciones.UniformeDiscreta import UniformeDiscreta

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        label = tk.Label(text="Distribuciones")
        label.place()
        p1 = Exponencial(self)
        p2 = Erlang(self)
        p3 = Normal(self)
        p4 = UnifomeContinua(self)
        p5 = Binomial(self)
        p6 = Poisson(self)
        p7 = Geometrica(self)
        p8 = UniformeDiscreta(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Distribucion Exponencial", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Distribucion Erlang", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Distribucion Normal", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Distribucion Unifome Continua", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Distribucion Binomial", command=p5.lift)
        b6 = tk.Button(buttonframe, text="Distribucion Poisson", command=p6.lift)
        b7 = tk.Button(buttonframe, text="Distribucion Geometrica", command=p7.lift)
        b8 = tk.Button(buttonframe, text="Distribucion Uniforme Discreta", command=p8.lift)
        
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")
        b8.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulador de Numeros Aleatorios")
    main = MainView(root)

    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1200x680")
    root.mainloop()