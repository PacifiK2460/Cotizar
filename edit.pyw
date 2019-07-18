from tkinter import *
import tkinter as Tkinter
import tkinter.ttk as ttk
import pandas as pd
from tkinter import messagebox
import csv

ancho = 1000
alto = 230

def actualizar():
    print("NP : {} | Type: {}".format(newprice.get(),type(newprice.get())))
    idv = int(idVar.get())
    #print("Precio : {}".format())

    df = pd.read_csv("datos.csv")
    print("Precio anterior : {}".format(df.at[idv,'Precio']))
    df.iat[idv,5] = newprice.get()
    print("Nuevo precio : {}".format(df.at[idv,'Precio']))
    df.to_csv("datos.csv", index=False)

    print("-------------------------------------------------------")

    #messagebox.showinfo("Atención","Precio de {} actualizado a {}".format(row[0],newprice.grt()))
    

def ventana_edit():

    idv = int(idVar.get())

    data = pd.read_csv("datos.csv",index_col="ID")
    row = data.loc[idv]

    root=Tkinter.Tk()
    root.title("Edición de datos.")
    root.iconbitmap("logo.ico")
    root.geometry("320x90")
    root.resizable(0,0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.config(background="lavender")

    width = root.winfo_width() 
    height = root.winfo_height() 
    x = (root.winfo_screenwidth() // 2) - (width // 2) 
    y = (root.winfo_screenheight() // 2) - (height // 2) 
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    txt = Label(root,text="El precio anterior de {} era de ${}".format(row[0],row[4]))
    print("Producto: {} | Precio: {}".format(row[0],row[4]))
    txt.place(x=0,y=0)
    chg = Label(root,text="El precio actualizado será de: $")
    chg.place(x=0,y=20)
    newprice = StringVar()
    print("NP : {} | Type: {}".format(newprice.get(),type(newprice.get())))
    box = Entry(root,textvariable = newprice)
    print("NP : {} | Type: {}".format(newprice.get(),type(newprice.get())))
    box.place(x=165,y=22)

    edit = Button(root,text="Actualizar",font=("Bold",13),fg="White",bg ="#4094da",command=actualizar)
    edit.place(x=5,y=50)
    salir = Button(root,text="Cancelar",fg = "White",bg = "#e7513a",font=("Bold",13),command=root.quit)
    salir.place(x=235,y=50)    

def buscar():
    if idVar.get().isdigit() == False:
        messagebox.showerror("Error","El ID dado tiene que ser un numero.")
    else:

        idv = int(idVar.get())
        
        if idv >= maxId:
            messagebox.showerror("Error","ID inexistente.")
        else:
            ventana_edit()

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

#
idVar = StringVar()
newprice = StringVar()
print("NP : {} | Type: {}".format(newprice.get(),type(newprice.get())))
#

tabla = ttk.Treeview(columns=('Material','Medidas','Calibre','desarolloarollo','Precio'))

tabla.heading('#0', text='ID')
tabla.heading('#1', text='Material')
tabla.heading('#2', text='Medidas')
tabla.heading('#3', text='Calibre')
tabla.heading('#4', text='desarolloarollo')
tabla.heading('#5', text='Precio')

tabla.column('#0', minwidth=0,width=50)
tabla.column('#1', minwidth=0,width=189)
tabla.column('#2', minwidth=0,width=189)
tabla.column('#3', minwidth=0,width=189)
tabla.column('#4', minwidth=0,width=189)
tabla.column('#5', minwidth=0,width=189)


#Faltan añadir todos los datos, estos son solo Test's
with open('datos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    maxId = 0
    for row in csv_reader:
        if line_count != 0:
            tabla.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
            maxId+=1
        else:
            line_count+=1

print("1.- " + str(maxId))

tabla.pack()


txt = Label(window,text="Para editar algun valor, introdusca su ID y pulse '"'Buscar Datos'"':")
txt.place(x=ancho-(ancho-125),y=alto-35)
idBox = Entry(window,textvariable=idVar)
idBox.place(x=ancho-(ancho-460),y=alto-35)

edit = Button(window,text="Buscar Datos",font=("Bold",13),fg="White",bg ="#4094da",command=buscar)
edit.place(x=ancho-(ancho-10),y=alto-40)
salir = Button(window,text="Salir",fg = "White",bg = "#e7513a",font=("Bold",13),command=window.quit)
salir.place(x=ancho-60,y=alto-40)

window.mainloop() 