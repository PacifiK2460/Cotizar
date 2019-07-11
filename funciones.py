from tkinter import *
from tkinter import messagebox
from docx import *
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def test(cop,cam):
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

    titulo = "Carroceria para caja seca {} copete para {}".format(cop,cam)
    doc = canvas.Canvas("test {}.pdf".format(num),pagesize=A4)
    doc.setFont('Helvetica-Bold',15)
    doc.drawString(40,810,titulo)
    doc.save()
    
    os.remove("num.txt")

    f = open("num.txt","w")
    f.write("{}".format(num+1))
    f.close()
