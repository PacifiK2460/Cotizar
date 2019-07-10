from tkinter import *
from tkinter import messagebox

def confirmar1():
    if messagebox.askokcancel("Confirmar","Se contizara una {}.\nAlto: {}\nAncho: {}\nLargo: {}".format(v.get().lower(),alto.get(),ancho.get(),large.get())):
       window.geometry("720x480")
       width = window.winfo_width() 
       height = window.winfo_height() 
       x = (window.winfo_screenwidth() // 2) - (width // 2) 
       y = (window.winfo_screenheight() // 2) - (height // 2) 

       op1.grid_forget()
       op2.grid_forget()
       btn.place_forget()
       salir.place_forget()
       largeNo.grid_forget()
       largeBox.grid_forget()
       anchoCaja.grid_forget()
       anchoNo.grid_forget()
       altoCaja.grid_forget()
       altoNo.grid_forget()

       #aqui mequede

def cg():
    h = v.get()
    if h == "Plataforma":
        altoCaja.config(state=DISABLED)
        altoNo.config(state=DISABLED)
    else:
        altoNo.config(state=NORMAL)
        altoCaja.config(state=NORMAL)

window = Tk()
window.title("Cotizar")
window.geometry("190x150")
window.resizable(0,0)
window.iconbitmap("logo.ico")

width = window.winfo_width() 
height = window.winfo_height() 
x = (window.winfo_screenwidth() // 2) - (width // 2) 
y = (window.winfo_screenheight() // 2) - (height // 2) 
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

v = StringVar()
op1 = Radiobutton(window,text="Plataforma",variable=v,value="Plataforma",command=cg)
op1.grid(row=3,column=0)
op2 = Radiobutton(window,text="Caja seca",variable=v,value="Caja seca",command=cg)
op2.grid(row=3,column=1)

btn = Button(window,text="Siguiente",fg="Green",command=confirmar1)
btn.place(x=10,y=118)
salir = Button(window,text="Salir",fg="Red",command=window.quit)
salir.place(x=150,y=118)

large = IntVar()
largeNo = Label(window,text="Largo: ",font="Bold")
largeNo.grid(row=0,column=0)
largeBox = Entry(window,textvariable = large)
largeBox.grid(row = 0, column = 1)

ancho = IntVar()
anchoNo = Label(window,text="Ancho: ",font="Bold")
anchoNo.grid(row=1,column=0)
anchoCaja = Entry(window,textvariable = ancho)
anchoCaja.grid(row = 1, column = 1)

alto = IntVar()
altoNo = Label(window,text="Alto: ",font="Bold")
altoNo.grid(row=2,column=0)
altoCaja = Entry(window,textvariable = alto)
altoCaja.grid(row = 2, column = 1)

window.mainloop()
