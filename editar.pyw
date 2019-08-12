import pandas as pd 
from tkinter import *
import tkinter as Tkinter
from tkinter import messagebox
import glob
import subprocess
import os
 
def actualizar():
    cont = True
    try:
        df = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
        print("Precio anterior : {}".format(df.at[idv,'Precio']))
        df.iat[idv,6] = price.get()
        print("Nuevo precio : {}".format(df.at[idv,'Precio']))
        df.to_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv", index=False)
    except PermissionError:
        messagebox.showerror("Error","No se pudo escribir y guardar los cambios hechoes en el archivo, por favor, cierre otras aplicaciones que puedan estar usandolo.")
        cont = False

    print("-------------------------------------------------------")

    if cont == True:
        if messagebox.askyesno("Atención","Precio de {} actualizado a {}. ¿Desea actualizar más precios?".format(row[0],price.get())):
            root.destroy()
            subprocess.Popen("python C:/Users/trabajo/Desktop/Cotizar/cotizar-1/edit.pyw",shell=False)
        else:
            root.destroy()

f = open("idv.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
idv = int(f.readline())
f.close()

for fl in glob.glob("idv.txt"):
    os.remove(fl)

data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv",index_col="ID")
row = data.loc[idv]

root=Tkinter.Tk()
root.title("Edición de datos.")
root.iconbitmap("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/logo.ico")
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

txt = Label(root,text="El precio anterior de {} era de ${}".format(row[0],row[5]))
print("Producto: {} | Precio: {}".format(row[0],row[4]))
txt.place(x=0,y=0)
chg = Label(root,text="El precio actualizado será de: $")
chg.place(x=0,y=20)
price = StringVar()
idBox = Entry(root,textvariable=price)
idBox.focus_force()
idBox.place(x=165,y=22)

edit = Button(root,text="Actualizar",font=("Bold",13),fg="White",bg ="#4094da",command=actualizar)
edit.place(x=5,y=50)
salir = Button(root,text="Cancelar",fg = "White",bg = "#e7513a",font=("Bold",13),command=root.quit)
salir.place(x=235,y=50)

root.mainloop()