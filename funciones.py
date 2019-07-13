from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from docx import *
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table
from reportlab.lib import colors
import subprocess
import os

class Caracteristicas:
    def __init__(self,name, des, price):
        self.set_name(name)
        self.set_des(des)
        self.set_price(price)
    
    def set_name(self,name):
        self._name = name
    def set_price(self,price):
        self._price = price
    def set_des(self,des):
        self._des = des

    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
    def get_des(self):
        return self._des

    def print_price(self):
        print("El precio de {} = {}".format(self.get_name(),self.get_price()))
    def print_des(self):
        print("El desarollo de {} = {}".format(self.get_name(),self.get_des()))

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Cotización")
        
        self.progressbar = ttk.Progressbar(self,mode="indeterminate")
        self.progressbar.place(x=30, y=60, width=220)
        self.place(width=300, height=200)
        main_window.geometry("300x100")

def imprimir_cot(cop,cam,alto,ancho,largo):

    f = open("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/cop","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    print("Se ah creado el archivo cap")
    f.write(cop)
    print("Se ah escrito en el")
    f.close() #lo cierra
    print("Se ah cerrado")

    f = open("cam.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    f.write(cam)
    f.close() #lo cierra

    f = open("alto.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    f.write(alto)
    f.close() #lo cierra
    
    f = open("ancho.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    f.write(ancho)
    f.close() #lo cierra

    f = open("largo.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    f.write(largo)
    f.close() #lo cierra    

    main_window = tk.Tk()
    main_window.resizable(0,0)
    app = Application(main_window)
    app.progressbar.start(10)
    process1 = subprocess.call(['python', 'imp_cot.py'])
    app.mainloop()

#os.remove("cop.txt") #Elimina ese archivo de numero
#s.remove("cam.txt") #Elimina ese archivo de numero
#os.remove("alto.txt") #Elimina ese archivo de numero
#os.remove("ancho.txt") #Elimina ese archivo de numero
#os.remove("largo.txt") #Elimina ese archivo de numero
