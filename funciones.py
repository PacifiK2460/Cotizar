from tkinter import *
from tkinter import messagebox
from docx import *
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def test(cop,cam,alto,ancho,largo):
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
    
    f = open("num.txt","r+") #Abre el archivo ñee el ultimo numero y lo guarad en una variable
    num = int(f.readline())
    print("Numero leido: {}".format(num))
    f.close() #lo cierra

    titulo = "Carroceria para caja seca {} copete para {}".format(cop,cam).upper()
    doc = canvas.Canvas("Carroceria para caja seca {} copete para {} ({}).pdf".format(cop,cam,num),pagesize=A4)
    doc.setFont('Helvetica-Bold',15)
    doc.drawString(40,810,titulo) #Escribe el top del titulo

    doc.drawString(40,770,"MEDIDAS:") #Escribe lasmedidas 
    doc.drawString(40,750,"LARGO:    {} mts.".format(largo))
    doc.drawString(40,730,"ANCHO:    {} mts.".format(ancho))
    doc.drawString(40,710,"ALTO:     {} mts.".format(alto))

    doc.drawImage("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/dibujos/caja seca/sin copete/caja seca camion isuzu labuena - copia.bmp",380,610,preserveAspectRatio=True,width=170)

    doc.save()
    
    os.remove("num.txt") #Elimina ese archivo de numero

    f = open("num.txt","w") #Crea otro archio con el mismo numero
    f.write("{}".format(num+1)) #Escribo el numero del archivo anterior + 1
    f.close() #Cierra el numerp
