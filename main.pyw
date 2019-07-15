from tkinter import *
from tkinter import messagebox
from cotizar import *

def ver():
    master.withdraw()
    os.system("python cotizar.pyw")

def editar_dat():
    messagebox.askokcancel("Proceder","Se van a editar los datos.")

if __name__ == '__main__':

    #Incio de ventana
    master = Tk()
    master.title("Inicio")
    master.geometry("200x100") #Tam. original: 245x180
    master.resizable(0,0)
    master.iconbitmap("logo.ico")

    width = master.winfo_width() 
    height = master.winfo_height() 
    x = (master.winfo_screenwidth() // 2) - (width // 2) 
    y = (master.winfo_screenheight() // 2) - (height // 2) 
    master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
    s = bool
    h = StringVar()
        
    cotizar = Button(master,text="Cotizar",font=("Bold",13),fg="Green",command=ver)
    cotizar.pack()
    editar = Button(master,text="Editar datos",font=("Bold",13),fg="Green",command=editar_dat)
    editar.pack()

    salir = Button(master,text="Salir",font=("Bold",13),fg="Red",command=master.quit)
    salir.pack()

    master.mainloop()