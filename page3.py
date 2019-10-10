
import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
from time import time
import seaborn as sns
from Page import Page
import tempfile
class Page3(Page):
    def __init__(self, *args, **kwargs): 
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        label.pack(side="top")

        #Bloque lam
        label_lam = tk.Label(self,text="Seleccione Metodo")
        label_lam.pack(side="top")

        OptionList = ["Teorema Central del Limite","Algoritmo de Box Muller"] 
        variable = tk.StringVar(self)
        variable.set(OptionList[0])

        w = tk.OptionMenu(self, variable, *OptionList)
        w.pack()      


        #Bloque Muestras
        label_muestras = tk.Label(self,text="Ingrese cantidad de muestras")  
        label_muestras.pack()
        self.muestras = tk.Entry(self)
        self.muestras.pack()
    
        #Boton Simular
        self.simular = tk.Button(self, text="Simular",command=self.simular)
        self.simular.pack()

        #Almacenamiento de Estado
        self.temporal_page3 = tempfile.TemporaryFile()
        self.temporal_page3.write(b'0')

        #Canvas
        self.canvas = tk.Canvas(self, width=600, height=400, background="black")
        self.fig = plt.figure()

    def normal_BoxMuller(self,muestras):
        X = []
        U1 = self.Random(muestras)
        U2 = self.Random(muestras)
        for i in range(muestras):
            
            x = -2*np.log(U1[i])
            x = x**(1/2)
            x = x*np.cos(2*np.pi*U2[i])
            X.append(x)
            
            y = -2*np.log(U1[i])
            y = y**(1/2)
            y = y*np.cos(2*np.pi*U2[i])
            X.append(y)
        return X

    def normal(self,muestras): 
        X = [] 
        for i in range(muestras):
            X.append(((sum(self.Random(muestras))-(muestras/2))/(np.sqrt(muestras/12)))) 
        return(X)

    def simular(self):
        self.temporal_page3.seek(0)
        if(self.temporal_page3.read() == b'0'):
            x = self.normal_BoxMuller(int(self.muestras.get()))
            #Grafica
            sns.set()
            fig = Figure(figsize=(2, 2), dpi=100)
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c')

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            #Almacenamiento del Estado
            self.temporal_page3.close()
            self.temporal_page3 = tempfile.TemporaryFile()
            self.temporal_page3.write(b'1')
        else:
            self.canvas.get_tk_widget().destroy()
            x = self.normal_BoxMuller(int(self.muestras.get()))
            
            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.temporal_page3.close()
            self.temporal_page3 = tempfile.TemporaryFile()
            self.temporal_page3.write(b'1')