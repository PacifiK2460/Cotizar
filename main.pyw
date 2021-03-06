
from tkinter import *
from tkinter import messagebox
import subprocess

def ver():
    master.destroy()
    subprocess.Popen("python C:/Users/trabajo/Desktop/Cotizar/cotizar-1/cotizar.pyw",shell=False)

def editar_dat():
    if messagebox.askokcancel("Proceder","Se van a editar los datos."):
        master.destroy()
        subprocess.Popen("python C:/Users/trabajo/Desktop/Cotizar/cotizar-1/edit.pyw",shell=False)

if __name__ == '__main__':
    #Incio de ventanaOR
    master = Tk()
    master.title("Inicio")
    master.geometry("200x125")
    master.resizable(0,0)
    master.iconbitmap("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/logo.ico")

    width = master.winfo_width() 
    height = master.winfo_height() 
    x = (master.winfo_screenwidth() // 2) - (width // 2) 
    y = (master.winfo_screenheight() // 2) - (height // 2) 
    master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    cotizar = Button(master,text="Cotizar",font=("Bold",13),fg="White",bg ="#4094da",command=ver)
    cotizar.pack(pady=5)
    editar = Button(master,text="Editar datos",font=("Bold",13),fg="White",bg ="#09cb72",command=editar_dat)
    editar.pack(pady=5)
    salir = Button(master,text="Salir",font=("Bold",13),fg = "White",bg = "#e7513a",command=master.quit)
    salir.pack(pady=5)

    master.mainloop()