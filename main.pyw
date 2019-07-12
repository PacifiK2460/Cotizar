from funciones import *
from tkinter import *
from tkinter import messagebox

def confirmar1(): #Confirma accion delusuar

    if v.get() == "Caja seca":
        if c.get() == "camión":
                if messagebox.askokcancel("Confirmar","Se contizara una {} {} copete para {}.\n\nAlto: {}\nAncho: {}\nLargo: {}".format(v.get().lower(),cop.get().lower(),c.get(),alto.get(),ancho.get(),large.get())):
                 window.withdraw()
                 test(cop.get(),c.get(),alto.get(),ancho.get(),large.get())
        else:
                if messagebox.askokcancel("Confirmar","Se contizara una {} {} copete para {}.\n\nAlto: {}\nAncho: {}\nLargo: {}".format(v.get().lower(),cop.get().lower(),c.get(),alto.get(),ancho.get(),large.get())):
                 window.withdraw()
                 test(cop.get(),c.get(),alto.get(),ancho.get(),large.get())
    elif messagebox.askokcancel("Confirmar","Se contizara una {}.\n\nAncho: {}\nLargo: {}".format(v.get().lower(),ancho.get(),large.get())):
        window.withdraw()
            

def cg(): #Actualizar opcion de Alto segun Plataforma o Caja seca
    h = v.get()
    if h == "Plataforma":
        altoCaja.config(state=DISABLED)
        altoNo.config(state=DISABLED)
        btn.place(x=10,y=140)
        salir.place(x=185,y=140)
        window.geometry("245x180")
        conCopete.place(x=7,y=130)
        sinCopete.place(x=122,y=130)
        conCopete.place_forget()
        sinCopete.place_forget()

        op3.place(x=7,y=130)
        op4.place(x=122,y=130)
        op3.place_forget()
        op4.place_forget()
    else:
        altoNo.config(state=NORMAL)
        altoCaja.config(state=NORMAL)
        btn.place(x=10,y=190)
        salir.place(x=185,y=190)
        window.geometry("245x230")        
        conCopete.place(x=7,y=130)
        sinCopete.place(x=122,y=130)

        op3.place(x=7,y=158)
        op4.place(x=122,y=158)


#Incio de ventana
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
cop = StringVar()
conCopete = Radiobutton(window,text="Con copete",font=("Bold",13),variable=cop,value="con")
sinCopete = Radiobutton(window,text="Sin copete",font=("Bold",13),variable=cop,value="sin")

c = StringVar()
op3 = Radiobutton(window,text="Camión",font=("Bold",13),variable=c,value="camión",command=cg)
op4 = Radiobutton(window,text="Camioneta",font=("Bold",13),variable=c,value="camioneta",command=cg)

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