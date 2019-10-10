import tkinter as tk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt
from time import time
N = 100000

#Vistas
from page1 import Page1
from page2 import Page2
from page3 import Page3
from page4 import Page4
from page5 import Page5
from page6 import Page6
from page7 import Page7

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        label = tk.Label(text="Distribuciones")
        label.place()
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Page7(self)

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

        b1 = tk.Button(buttonframe, text="Distribucion Exponencial", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Distribucion Erlang", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Distribucion Normal", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Distribucion Unifome Continua", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Distribucion Binomial", command=p5.lift)
        b6 = tk.Button(buttonframe, text="Distribucion Poisson", command=p6.lift)
        b7 = tk.Button(buttonframe, text="Distribucion Geometrica", command=p7.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulador de Numeros Aleatorios")
    main = MainView(root)

    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1200x680")
    root.mainloop()