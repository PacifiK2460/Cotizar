from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
import pandas as pd
from tkinter import messagebox
import os
import csv

ancho = 1000
alto = 275

class Dato:
    def set_id(self,id):
        self._id=id
    def set_max(self,maximo):
        self._max=maximo

    def get_id(self):
        return self._id
    def get_max(self):
        return self._max

objeto = Dato()

def buscar():
    objeto.set_id(idv1.get())
    if objeto.get_id().isdigit() == False:
         messagebox.showerror("Error","El ID dado tiene que ser un numero.")
         print(objeto.get_id())
    else:

        idv = int(objeto.get_id())
        if idv >= objeto.get_max():
            messagebox.showerror("Error","ID inexistente.")
            print(objeto.get_id())
        else:
            f = open("idv.txt","w+")
            f.write(str(idv))
            f.close()
            window.withdraw()
            os.system("python editar.pyw")

window=Tkinter.Tk()
window.title("Edición de datos.")
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

tabla = ttk.Treeview(columns=('Material','Medidas','Calibre','desarollo','Peso','Precio'))

tabla.heading('#0', text='ID')
tabla.heading('#1', text='Material')
tabla.heading('#2', text='Medidas')
tabla.heading('#3', text='Calibre')
tabla.heading('#4', text='desarollo')
tabla.heading('#5',text="Peso")
tabla.heading('#6', text='Precio')

tabla.column('#0', minwidth=0,width=50)
tabla.column('#1', minwidth=0,width=420)
tabla.column('#2', minwidth=0,width=120)
tabla.column('#3', minwidth=0,width=70)
tabla.column('#4', minwidth=0,width=70)
tabla.column('#5', minwidth=0,width=90)
tabla.column('#6', minwidth=0,width=180)

    #Faltan añadir todos los datos, estos son solo Test's
with open('datos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    maxId = 0
    for row in csv_reader:
        if line_count != 0:
            tabla.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
            maxId+=1
        else:
            line_count+=1

print("1.- " + str(maxId))
objeto.set_max(maxId)


tabla.pack()

txt = Label(window,text="Para editar algun valor, introdusca su ID y pulse '"'Buscar Datos'"':")
txt.place(x=ancho-(ancho-125),y=alto-35)
   
idv1 = StringVar()
idBox = Entry(window,textvariable=idv1)
idBox.place(x=ancho-(ancho-460),y=alto-35)
idBox.focus()

edit = Button(window,text="Buscar Datos",font=("Bold",13),fg="White",bg ="#4094da",command=buscar)
edit.place(x=ancho-(ancho-10),y=alto-40)
salir = Button(window,text="Salir",fg = "White",bg = "#e7513a",font=("Bold",13),command=window.quit)
salir.place(x=ancho-60,y=alto-40)

window.mainloop() 