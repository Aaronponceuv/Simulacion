
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
from Distribuciones.Page import Page
import tempfile

class Geometrica(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        #Elementos
        lbl = tk.Label(self, text="Distribucción Geométrica", font=("Arial Bold", 20)).pack()
        label = tk.Label(self, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        label.pack(side="top")

        #Bloque lam
        label_prob = tk.Label(self,text="Ingrese el Valor de Probabilidad")
        label_prob.pack(side="top")
        self.prob = tk.Entry(self) 
        self.prob.pack()       

        #Bloque Muestras
        label_muestras = tk.Label(self,text="Ingrese cantidad de muestras")  
        label_muestras.pack()
        self.muestras = tk.Entry(self)
        self.muestras.pack()
    
        #Boton Simular
        self.simular = tk.Button(self, text="Simular",command=self.simular)
        self.simular.pack()

        #Almacenamiento de Estado
        self.temporal_Geometrica = tempfile.TemporaryFile()
        self.temporal_Geometrica.write(b'0')

        #Canvas
        self.canvas = tk.Canvas(self, width=600, height=400, background="black")
        self.fig = plt.figure()

    def simular(self):
        self.temporal_Geometrica.seek(0)
        if(self.temporal_Geometrica.read() == b'0'):

            x = self.geometrica(float(self.prob.get()),int(self.muestras.get()))
            #Grafica
            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            plt.title('Histograma de la Distribución Geometrica')
            plt.xlabel('$x$')
            plt.ylabel('Frecuencia de $x$')
            plt.grid(True)

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            #Almacenamiento del Estado
            self.temporal_Geometrica.close()
            self.temporal_Geometrica = tempfile.TemporaryFile()
            self.temporal_Geometrica.write(b'1')
        else:
            self.canvas.get_tk_widget().destroy()
            x = self.geometrica(float(self.prob.get()),int(self.muestras.get()))

            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            plt.title('Histograma de la Distribución Geometrica')
            plt.xlabel('$x$')
            plt.ylabel('Frecuencia de $x$')
            plt.grid(True) 
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.temporal_Geometrica.close()
            self.temporal_Geometrica = tempfile.TemporaryFile()
            self.temporal_Geometrica.write(b'1')

    def geometrica(self,p,muestras):
        U = self.Random(muestras)
        X = []
        for i in range(muestras):
            X.append(1+(np.log(U[i])/(np.log(1-p))))
        return(X)
