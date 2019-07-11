from tkinter import *
from tkinter import messagebox
from docx import *
from docx import Document
import os

def test():
    window = Tk()
    window.title("Cotizando")
    window.geometry("245x180")
    window.resizable(0,0)
    window.iconbitmap("logo.ico")

    #centro de ventana
    width = window.winfo_width() 
    height = window.winfo_height() 
    x = (window.winfo_screenwidth() // 2) - (width // 2) 
    y = (window.winfo_screenheight() // 2) - (height // 2) 
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    f = open("num.txt","r+")
    num = int(f.readline())
    print("Numero leido: {}".format(num))
    f.close()

    document = Document()
    table = document.add_table(rows=23, cols=5)
    document.save("cotizacion {}.docx".format(num))

    os.remove("num.txt")

    f = open("num.txt","w")
    f.write("{}".format(num+1))
    f.close()
    

