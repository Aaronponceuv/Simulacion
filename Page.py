import tkinter as tk
from time import time
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

    def Random(self,ciclo):
        X = []
        a = 16807
        m = (2**31) -(1)
        b = 0
        Xn = time() #semilla (debe cambiar para generar la Erlang, no se me ocurrio otro metodo para hacerla variar)
        for i in range(ciclo):
            Xn1 = self.formula(a,b,Xn,m)
            ri = self.aleatorio(Xn1,m)
            X.append(ri)
            Xn = Xn1
        return X
    
    def formula(self,a,b,Xn,m):
        return ((a*Xn+b)%m)
    
    def aleatorio(self,Xn1,m):
        return Xn1/m