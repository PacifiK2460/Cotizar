from funciones import *
from tkinter import *
from tkinter import messagebox

def confirmar1(): #Confirma accion delusuar
    if messagebox.askokcancel("Confirmar","Se contizara una {}.\nAlto: {}\nAncho: {}\nLargo: {}".format(v.get().lower(),alto.get(),ancho.get(),large.get())):

       window.withdraw()

       test()

def cg(): #Actualizar opcion de Alto segun Plataforma o Caja seca
    h = v.get()
    if h == "Plataforma":
        altoCaja.config(state=DISABLED)
        altoNo.config(state=DISABLED)
    else:
        altoNo.config(state=NORMAL)
        altoCaja.config(state=NORMAL)

#Incio de ventana

if __name__ == "__main__":
    window = Tk()
    window.title("Cotizar")
    window.geometry("245x180")
    window.resizable(0,0)
    window.iconbitmap("logo.ico")

    #centro de ventana
    width = window.winfo_width() 
    height = window.winfo_height() 
    x = (window.winfo_screenwidth() // 2) - (width // 2) 
    y = (window.winfo_screenheight() // 2) - (height // 2) 
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    #Cajas de texto y texto de la ventana
    v = StringVar()
    op1 = Radiobutton(window,text="Plataforma",font=("Bold",13),variable=v,value="Plataforma",command=cg)
    op1.place(x=7,y=102)
    op2 = Radiobutton(window,text="Caja seca",font=("Bold",13),variable=v,value="Caja seca",command=cg)
    op2.place(x=122,y=102)

    large = StringVar()
    largeNo = Label(window,text="Largo: ",font=("Bold",17))
    largeNo.grid(row=0,column=0)
    largeBox = Entry(window,textvariable = large)
    largeBox.grid(row = 0, column = 1)
    largeBox.focus()

    ancho = StringVar()
    anchoNo = Label(window,text="Ancho: ",font=("Bold",17))
    anchoNo.grid(row=1,column=0)
    anchoCaja = Entry(window,textvariable = ancho)
    anchoCaja.grid(row = 1, column = 1)

    alto = StringVar()
    altoNo = Label(window,text="Alto: ",font=("Bold",17))
    altoNo.grid(row=2,column=0)
    altoCaja = Entry(window,textvariable = alto)
    altoCaja.grid(row = 2, column = 1)

    btn = Button(window,text="Siguiente",font=("Bold",13),fg="Green",command=confirmar1)
    btn.place(x=10,y=140)
    salir = Button(window,text="Salir",font=("Bold",13),fg="Red",command=window.quit)
    salir.place(x=185,y=140)

    #Porgrama tecnico

    window.mainloop() #Loop, ventana permanentemente escuchando el user's input