from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
import csv

def agregar_datos():
    pass

ancho = 1000
alto = 230

window=Tkinter.Tk()
window.title("Edición de datos")
window.iconbitmap("logo.ico")
window.geometry("{}x{}".format(ancho,alto))
window.resizable(0,0)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.config(background="lavender")

width = window.winfo_width() 
height = window.winfo_height() 
x = (window.winfo_screenwidth() // 2) - (width // 2) 
y = (window.winfo_screenheight() // 2) - (height // 2) 
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

tabla = ttk.Treeview(columns=('Material','Medidas','Calibre','Desarollo','Precio'))

tabla.heading('#0', text='Material')
tabla.heading('#1', text='Medidas')
tabla.heading('#2', text='Calibre')
tabla.heading('#3', text='Desarollo')
tabla.heading('#4', text='Precio')

tabla.column('#1', stretch=Tkinter.NO)
tabla.column('#2', stretch=Tkinter.NO)
tabla.column('#0', stretch=Tkinter.NO)

tabla.pack()

agregar = Button(window,text="Agregar datos",fg="White",bg ="#4094da",font=("Bold",13),command=agregar_datos)
agregar.place(x=ancho-(ancho-10),y=alto-40)
salir = Button(window,text="Salir",fg = "White",bg = "#e7513a",font=("Bold",13),command=window.quit)
salir.place(x=ancho-60,y=alto-40)

window.mainloop()