from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
import csv
import os

def agregar_datos(nombre,medidas,calibre,desarollo,precio):
    data =  [["Nombre","Medidas","Calibre","Desarollo","Precio"],
            [nombre,medidas,calibre,desarollo,precio]]

    archivo = open('datos.csv', 'w')
    with archivo:
        writer = csv.writer(archivo)
        writer.writerows(data)           
        messagebox.showinfo("Atención","Datos agregados exitosamente")

def agregar2():
    root = Tk()
    root.title("Ingresar datos")
    root.iconbitmap("logo.ico")
    ancho2 = 255
    alto2= 350
    width = root.winfo_width() 
    height = root.winfo_height() 
    x = (root.winfo_screenwidth() // 2) - (width // 2) 
    y = (root.winfo_screenheight() // 2) - (height // 2) 
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.geometry("{}x{}".format(ancho2,alto2))
    root.resizable(0,0)

    nombre = StringVar()
    nomNo = Label(root,text="Material: ",font=("Bold",16))
    nomNo.grid(row=0, column=0,pady=5,padx=5)
    nomBox = Entry(root,textvariable = nombre)
    nomBox.grid(row=0, column=1)

    medidas = StringVar()
    medNo = Label(root,text="Medidas: ",font=("Bold",16))
    medNo.grid(row=1, column=0,pady=5,padx=5)
    medBox = Entry(root,textvariable = medidas)
    medBox.grid(row=1, column=1,pady=5,padx=5)

    calibre = StringVar()
    calNo = Label(root,text="Calibre: ",font=("Bold",16))
    calNo.grid(row=2, column=0,pady=5,padx=5)
    calBox = Entry(root,textvariable = calibre)
    calBox.grid(row=2, column=1)

    desarollo = StringVar()
    desNo = Label(root,text="Desarollo: ",font=("Bold",16))
    desNo.grid(row=3, column=0,pady=5,padx=5)
    desBox = Entry(root,textvariable = desarollo)
    desBox.grid(row=3, column=1)

    precio = StringVar()
    preNo = Label(root,text="Precio: ",font=("Bold",16))
    preNo.grid(row=4, column=0,pady=5,padx=5)
    preBox = Entry(root,textvariable = precio)
    preBox.grid(row=4, column=1)

    nota = Label(root,text="Nota: Si el material no lleva algun \nparametro, simplemente pon dos '"'--'"' \n(guiones medio).",font=("Bold",10),anchor="w")
    nota.place(x=25,y=200)

    agregar = Button(root,text="Agregar datos",fg="White",bg ="#4094da",font=("Bold",13),command=agregar_datos(nombre.get(),medidas.get(),calibre.get(),desarollo.get(),precio.get()))
    agregar.place(x=ancho2-(ancho2-10),y=alto2-40)
    cancelar = Button(root,text="Cancelar",fg = "White",bg = "#e7513a",font=("Bold",13),command=root.withdraw)
    cancelar.place(x=ancho2-90,y=alto2-40)

if __name__ == '__main__':
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

    agregar = Button(window,text="Agregar datos",fg="White",bg ="#4094da",font=("Bold",13),command=agregar2)
    agregar.place(x=ancho-(ancho-10),y=alto-40)
    salir = Button(window,text="Salir",fg = "White",bg = "#e7513a",font=("Bold",13),command=window.quit)
    salir.place(x=ancho-60,y=alto-40)

    window.mainloop()