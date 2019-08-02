from funciones import *
from tkinter import *
from tkinter import messagebox
from os import *
from main import *

def confirmar1(): #Confirma accion delusuar
        continuar = True
        window.update()
        window.update_idletasks()

        try:
                float(alto.get())
                window.update()
                window.update_idletasks()
        except ValueError:
                messagebox.showerror("Error","El alto debe ser un valor numerico")
                continuar = False
                window.update()
                window.update_idletasks()
        try:
                float(ancho.get())
                window.update()
                window.update_idletasks()
        except ValueError:
                messagebox.showerror("Error","El ancho debe ser un valor numerico")
                continuar = False
                window.update()
                window.update_idletasks()
        try:
                float(large.get())
                window.update()
                window.update_idletasks()
        except ValueError:
                messagebox.showerror("Error","El largo debe ser un valor numerico")
                continuar = False
                window.update()
                window.update_idletasks()

        window.update()
        window.update_idletasks()

        if continuar == True:
                if v.get() == "Caja seca":
                        if messagebox.askokcancel("Confirmar","Se contizara una {} {} copete para {}. \nTipo de precio: {}.\n\nAlto: {}\nAncho: {}\nLargo: {}".format(v.get().lower(),cop.get().lower(),c.get(),t_precio.get(),alto.get(),ancho.get(),large.get())):
                                window.withdraw()
                                imprimir_cot(cop.get(),c.get(),float(alto.get())*100,float(ancho.get())*100,float(large.get())*100,t_precio.get())
                                window.quit()
                elif messagebox.askokcancel("Confirmar","Se contizara una {}. \nTipo de precio: {}.\n\nAncho: {}\nLargo: {}".format(v.get().lower(),t_precio.get(),ancho.get(),large.get())):
                        window.withdraw()
            

def cg(): #Actualizar opcion de Alto segun Plataforma o Caja seca
    h = v.get()
    if h == "Plataforma":
        altoCaja.config(state=DISABLED)
        altoNo.config(state=DISABLED)
        #window.geometry("245x180")
        conCopete.grid(row=1,column=0)
        sinCopete.grid(row=1,column=1)
        conCopete.grid_forget()
        sinCopete.grid_forget()

        op3.grid(row=2,column=0)
        op4.grid(row=2,column=1)
        op3.grid_forget()
        op4.grid_forget()
        window.geometry("245x280")

    else:
        altoNo.config(state=NORMAL)
        altoCaja.config(state=NORMAL)
        window.geometry("245x340")        
        conCopete.grid(row=1,column=0)
        sinCopete.grid(row=1,column=1)

        op3.grid(row=2,column=0)
        op4.grid(row=2,column=1)

        btn.pack(side=LEFT,padx=5,pady=5)
        salir.pack(side=RIGHT,padx=5,pady=5)

if __name__ == '__main__':

        window = Tk()
        window.title("Cotizar")
        window.geometry("245x280") #Tam. original: 245x180
        window.resizable(0,0)
        window.iconbitmap("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/logo.ico")

        #centro de ventana
        width = window.winfo_width() 
        height = window.winfo_height() 
        x = (window.winfo_screenwidth() // 2) - (width // 2) 
        y = (window.winfo_screenheight() // 2) - (height // 2) 
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        #Cajas de texto y texto de la ventana
        labelframe = LabelFrame(window, text="Medidas")
        labelframe.pack(fill="both", expand="no",padx=7,pady=7)

        large = StringVar()
        largeNo = Label(labelframe,text="Largo: ",font=("Bold",17))
        largeNo.grid(row=0,column=0)
        largeBox = Entry(labelframe,textvariable = large)
        largeBox.grid(row = 0, column = 1)
        largeBox.focus()

        ancho = StringVar()
        anchoNo = Label(labelframe,text="Ancho: ",font=("Bold",17))
        anchoNo.grid(row=1,column=0)
        anchoCaja = Entry(labelframe,textvariable = ancho)
        anchoCaja.grid(row = 1, column = 1)

        alto = StringVar()
        altoNo = Label(labelframe,text="Alto: ",font=("Bold",17))
        altoNo.grid(row=2,column=0)
        altoCaja = Entry(labelframe,textvariable = alto)
        altoCaja.grid(row = 2, column = 1)

        #-----------------------------------------
        w = LabelFrame(window, text="Tipo")
        w.pack(fill="both", expand="yes",padx=7,pady=1)

        v = StringVar()
        op1 = Radiobutton(w,text="Plataforma",font=("Bold",13),variable=v,value="Plataforma",command=cg)
        op1.grid(row=0,column=0)
        op2 = Radiobutton(w,text="Caja seca",font=("Bold",13),variable=v,value="Caja seca",command=cg)
        op2.grid(row=0,column=1)
        cop = StringVar()
        conCopete = Radiobutton(w,text="Con copete",font=("Bold",13),variable=cop,value="con")
        sinCopete = Radiobutton(w,text="Sin copete",font=("Bold",13),variable=cop,value="sin")
        c = StringVar()
        op3 = Radiobutton(w,text="Camión",font=("Bold",13),variable=c,value="camión",command=cg)
        op4 = Radiobutton(w,text="Camioneta",font=("Bold",13),variable=c,value="camioneta",command=cg)

        p = LabelFrame(window,text="Precio")
        p.pack(fill="both", expand="yes",padx=7,pady=1)
        t_precio = StringVar()
        econ = Radiobutton(p,text="Economica",font=("Bold",13),variable=t_precio,value="economica")
        normal = Radiobutton(p,text="Normal",font=("Bold",13),variable=t_precio,value="normal")
        econ.grid(row=0,column=0)
        normal.grid(row=0,column=1)

        btn = Button(window,text="Siguiente",font=("Bold",13),fg="White",bg ="#4094da",command=confirmar1)
        btn.pack(side=LEFT,padx=5,pady=5)
        salir = Button(window,text="Salir",font=("Bold",13),fg = "White",bg = "#e7513a",command=window.quit)
        salir.pack(side=RIGHT,padx=5,pady=5)
        
        window.update()
        window.update_idletasks()
        window.mainloop() #Loop, ventana permanentemente escuchando el user's input