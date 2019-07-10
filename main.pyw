from tkinter import *
from tkinter import messagebox

def siguiente1(Large,Alto,Ancho):

    opcion = lista.get()

    window.iconify()

    messagebox.askokcancel(message="Se cotizará una " + opcion.lower() + ".\n Largo: " + str(Large) + ".\n Alto: " + str(Alto) + ".\n Ancho: " + str(Ancho) + ".\n", title="Cotizar")
 
    
def siguiente():

    opcion = lista.get()

    if opcion == 'Caja Seca':

        window.quit()

        root = Tk()
        root.title("Caja seca")
        root.geometry("200x125")
        root.resizable(0,0)
        root.iconbitmap("logo.ico")

        width = root.winfo_width() 
        height = root.winfo_height() 
        x = (root.winfo_screenwidth() // 2) - (width // 2) 
        y = (root.winfo_screenheight() // 2) - (height // 2) 
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 

        large = IntVar()
        largeNo = Label(root,text="Largo: ",font="Bold").grid(row=0,column=0)
        largeBox = Entry(root,textvariable = large).grid(row = 0, column = 1)

        ancho = IntVar()
        anchoNo = Label(root,text="Ancho: ",font="Bold").grid(row=1,column=0)
        anchoCaja = Entry(root,textvariable = ancho).grid(row = 1, column = 1)
        alto = IntVar()
        altoNo = Label(root,text="Alto: ",font="Bold").grid(row=2,column=0)
        altoCaja = Entry(root,textvariable = alto).grid(row = 2, column = 1)

        btn = Button(root,text="Siguiente",fg="Green",command=siguiente1(large.get(),alto.get(),ancho.get())).place(x=75,y=70)

        salir = Button(root,text="Salir",fg="Red",command=root.quit).place(x=85,y=100)



        root.mainloop()
    else:
        window.iconify()

        root = Tk()
        root.title("Plataforma")
        root.geometry("200x110")
        root.resizable(0,0)
        root.iconbitmap("logo.ico")

        width = root.winfo_width() 
        height = root.winfo_height() 
        x = (root.winfo_screenwidth() // 2) - (width // 2) 
        y = (root.winfo_screenheight() // 2) - (height // 2) 
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 

        large = IntVar()
        largeNo = Label(root,text="Largo: ",font="Bold").grid(row=0,column=0)
        largeBox = Entry(root,textvariable = large).grid(row = 0, column = 1)

        ancho = IntVar()
        anchoNo = Label(root,text="Ancho: ",font="Bold").grid(row=1,column=0)
        anchoCaja = Entry(root,textvariable = ancho).grid(row = 1, column = 1)

        btn = Button(root,text="Siguiente",fg="Green",command=siguiente1(large.get(),0,ancho.get())).place(x=65,y=50)

        salir = Button(root,text="Salir",fg="Red",command=root.quit).place(x=75,y=80)

        root.mainloop()
    

window = Tk()
window.title("Cotizar")
window.geometry("150x100")
window.resizable(0,0)
window.iconbitmap("logo.ico")

width = window.winfo_width() 
height = window.winfo_height() 
x = (window.winfo_screenwidth() // 2) - (width // 2) 
y = (window.winfo_screenheight() // 2) - (height // 2) 
window.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 


lista = StringVar(window)
lista.set("Plataforma")
w = OptionMenu(window,lista,"Caja Seca","Plataforma")
w.place(x=23,y=5)

btn = Button(window,text="Siguiente",fg="Green",command=siguiente).place(x=38,y=40)
salir = Button(window,text="Salir",fg="Red",command=window.quit).place(x=53,y=70)
    
window.mainloop()


