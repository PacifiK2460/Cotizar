from tkinter import *
from tkinter import messagebox
from cotizar import *

def ver():
    master.withdraw()
    os.system("python cotizar.pyw")

def editar_dat():
    if messagebox.askokcancel("Proceder","Se van a editar los datos."):
        master.withdraw()
        os.system("python edit.pyw")

if __name__ == '__main__':

    #Incio de ventana
    master = Tk()
    master.title("Inicio")
    master.geometry("200x125") #Tam. original: 245x180
    master.resizable(0,0)
    master.iconbitmap("logo.ico")

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