
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
class Binomial(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        lbl = tk.Label(self, text="Distribucción Binomial", font=("Arial Bold", 20)).pack()
        label = tk.Label(self, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        label.pack(side="top")

        #Bloque P
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
        self.temporal_Binomial = tempfile.TemporaryFile()
        self.temporal_Binomial.write(b'0')

        #Canvas
        self.canvas = tk.Canvas(self, width=600, height=400, background="black")
        self.fig = plt.figure()

    def ensayos_bernoulli(self,n,p):
        U = self.Random(n)
        X = []
        for i in range(n):
            if(U[i] <= p):
                X.append(1)
            else:
                X.append(0)
        return(X)
      
    def binomial(self,muestras,prob):
        X = []
        for i in range(muestras):
            X.append(sum(self.ensayos_bernoulli(muestras,prob)))
        return(X)

    def simular(self):
        self.temporal_Binomial.seek(0)
        if(self.temporal_Binomial.read() == b'0'):
            x = self.binomial(int(self.muestras.get()),float(self.prob.get()))
            #Grafica
            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            plt.title('Histograma de la Distribución Binomial')
            plt.xlabel('$x$')
            plt.ylabel('Frecuencia de $x$')
            plt.grid(True)

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            #Almacenamiento del Estado
            self.temporal_Binomial.close()
            self.temporal_Binomial = tempfile.TemporaryFile()
            self.temporal_Binomial.write(b'1')
        else:
            self.canvas.get_tk_widget().destroy()
            x = self.binomial(int(self.muestras.get()),float(self.prob.get()))

            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            plt.title('Histograma de la Distribución Binomial')
            plt.xlabel('$x$')
            plt.ylabel('Frecuencia de $x$')
            plt.grid(True) 
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.temporal_Binomial.close()
            self.temporal_Binomial = tempfile.TemporaryFile()
            self.temporal_Binomial.write(b'1')
