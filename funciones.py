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

    #Dibuja la carroceria
    #preserveAspectRatio=True
    doc.drawImage("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/dibujos/Sin título.png",0,310,preserveAspectRatio=True,width=600)

    doc.drawString(30,810,titulo) #Escribe el top del titulo

    doc.drawString(30,770,"MEDIDAS:") #Escribe lasmedidas 
    doc.drawString(30,750,"LARGO:")
    doc.drawString(30,730,"ANCHO:")
    doc.drawString(30,710,"ALTO:")
    
    doc.setFont('Helvetica-Bold',10)
    doc.drawString(95,750,"{} mts.".format(largo))
    doc.drawString(95,730,"{} mts.".format(ancho))
    doc.drawString(95,710,"{} mts.".format(alto))

    doc.save()
    
    os.remove("num.txt") #Elimina ese archivo de numero

    f = open("num.txt","w") #Crea otro archio con el mismo numero
    f.write("{}".format(num+1)) #Escribo el numero del archivo anterior + 1
    f.close() #Cierra el numerp
