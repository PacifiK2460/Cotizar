from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
import csv

ancho = 1000
alto = 230

def editar_datos():
    pass

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

tabla.heading('#0', text='ID')
tabla.heading('#1', text='Material')
tabla.heading('#2', text='Medidas')
tabla.heading('#3', text='Calibre')
tabla.heading('#4', text='Desarollo')
tabla.heading('#5', text='Precio')

tabla.column('#0', minwidth=0,width=50)
tabla.column('#1', minwidth=0,width=189)
tabla.column('#2', minwidth=0,width=189)
tabla.column('#3', minwidth=0,width=189)
tabla.column('#4', minwidth=0,width=189)
tabla.column('#5', minwidth=0,width=189)

with open('datos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 2
    for row in csv_reader:
        if line_count > 1:
            tabla.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        else:
            line_count+=1

print(line_count)


tabla.pack()

edit = Button(window,text="Editar Datos",font=("Bold",13),fg="White",bg ="#4094da",command=editar_datos)
edit.place(x=ancho-(ancho-10),y=alto-40)
salir = Button(window,text="Salir",fg = "White",bg = "#e7513a",font=("Bold",13),command=window.quit)
salir.place(x=ancho-60,y=alto-40)

window.mainloop() 