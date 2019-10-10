
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

class UnifomeContinua(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        lbl = tk.Label(self, text="Distribucción Uniforme Continua", font=("Arial Bold", 20)).pack()
        label = tk.Label(self, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        label.pack(side="top")

        #Bloque a
        label_a = tk.Label(self,text="Ingrese el Valor de a")
        label_a.pack(side="top")
        self.a = tk.Entry(self) 
        self.a.pack()       

        #Bloque b
        label_b = tk.Label(self,text="Ingrese b")  
        label_b.pack()
        self.b = tk.Entry(self)
        self.b.pack()

        #Bloque Muestras
        label_muestras = tk.Label(self,text="Ingrese cantidad de muestras")  
        label_muestras.pack()
        self.muestras = tk.Entry(self)
        self.muestras.pack()
    
        #Boton Simular
        self.simular = tk.Button(self, text="Simular",command=self.simular)
        self.simular.pack()

        #Almacenamiento de Estado
        self.temporal_UnifomeContinua = tempfile.TemporaryFile()
        self.temporal_UnifomeContinua.write(b'0')

        #Canvas
        self.canvas = tk.Canvas(self, width=600, height=400, background="black")
        self.fig = plt.figure()

    def uniforme(self,a,b,muestras):
        U = self.Random(muestras)
        X = []
        for i in range(muestras):
            X.append(a+(U[i]*(b-a)))
        return X

    def simular(self):
        self.temporal_UnifomeContinua.seek(0)
        if(self.temporal_UnifomeContinua.read() == b'0'):
            x = self.uniforme(int(self.a.get()),int(self.b.get()),int(self.muestras.get()))
            #Grafica
            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            plt.title('Histograma de la Distribución Uniforme Continua')
            plt.xlabel('$x$')
            plt.ylabel('Frecuencia de $x$')
            plt.grid(True)

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            #Almacenamiento del Estado
            self.temporal_UnifomeContinua.close()
            self.temporal_UnifomeContinua = tempfile.TemporaryFile()
            self.temporal_UnifomeContinua.write(b'1')
        else:
            self.canvas.get_tk_widget().destroy()
            x = self.uniforme(int(self.a.get()),int(self.b.get()),int(self.muestras.get()))

            sns.set()
            self.fig = plt.figure()
            plt.hist(x,density='True',bins=50,alpha=0.8,histtype='bar', edgecolor='c') 
            plt.title('Histograma de la Distribución Uniforme Continua')
            plt.xlabel('$x$')
            plt.ylabel('Frecuencia de $x$')
            plt.grid(True) 
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            self.temporal_UnifomeContinua.close()
            self.temporal_UnifomeContinua = tempfile.TemporaryFile()
            self.temporal_UnifomeContinua.write(b'1')