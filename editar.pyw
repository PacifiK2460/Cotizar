import pandas as pd 
from tkinter import *
import tkinter as Tkinter
from tkinter import messagebox
import os
 
def actualizar():
    df = pd.read_csv("datos.csv")
    print("Precio anterior : {}".format(df.at[idv,'Precio']))
    df.iat[idv,5] = price.get()
    print("Nuevo precio : {}".format(df.at[idv,'Precio']))
    df.to_csv("datos.csv", index=False)

    print("-------------------------------------------------------")

    root.withdraw()
    messagebox.showinfo("Atención","Datos editados exitosamente.")
                        #messagebox.showinfo("Atención","Precio de {} actualizado a {}".format(row[0],newprice.grt()))


f = open("idv.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
idv = int(f.readline())
f.close()

os.remove("idv.txt")

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
price = StringVar()
idBox = Entry(root,textvariable=price)
idBox.place(x=165,y=22)

edit = Button(root,text="Actualizar",font=("Bold",13),fg="White",bg ="#4094da",command=actualizar)
edit.place(x=5,y=50)
salir = Button(root,text="Cancelar",fg = "White",bg = "#e7513a",font=("Bold",13),command=root.quit)
salir.place(x=235,y=50)

root.mainloop()