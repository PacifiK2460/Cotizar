from tkinter import *
from tkinter import messagebox
from docx import *
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table
from reportlab.lib import colors
import os

width, height = A4

def __init__(self):
    pass

def test(cop,cam,alto,ancho,largo):
    window = Tk()
    window.title("Carroceria para caja seca {} copete para {}".format(cop,cam))
    window.geometry("245x180")
    #window.resizable(0,0)
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
    doc.setFont('Helvetica-Bold',13)

    #Dibuja la carroceria
    #preserveAspectRatio=True
    doc.drawImage("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/dibujos/Sin título.png",0,350,preserveAspectRatio=True,width=600)

    doc.drawString(30,825,titulo) #Escribe el top del titulo

    Alto = 790

    doc.drawString(30,Alto,"MEDIDAS:") #Escribe las medidas 
    doc.drawString(30,Alto-20,"LARGO:")
    doc.drawString(30,Alto-40,"ANCHO:")
    doc.drawString(30,Alto-60,"ALTO:")
    
    doc.setFont('Helvetica-Bold',10)
    doc.drawString(95,Alto-20,"{} mts.".format(largo))
    doc.drawString(95,Alto-40,"{} mts.".format(ancho))
    doc.drawString(95,Alto-60,"{} mts.".format(alto))

    data = [
        ["                                       MATERIAL","   CANTIDAD","  UNIDAD","     PRECIO","    TOTALES"],
        ["Material con lamina y maquila de varios calibres.","","","",""],
        ["PTR 4x3.","","","",""],
        ["PTR 4x2.","","","",""],
        ["Tubula 1''x1''. ","","","",""],
        ["Tubula 1 ½x 1 ½.","","","",""],
        ["Lamina aluminio.","","","",""],
        ["Madera piso 5/4,8,10.","","","",""],
        ["Triplay 6mm.","","","",""],
        ["Plafones 4'' led.","","","",""],
        ["Plafones 2'' led.","","","",""],
        ["Bragas 5/8.","","","",""],
        ["Vistas.","","","",""],
        ["Polin 3x3x8.","","","",""],
        ["Bisagra y Pasadores.","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""]
        ]

    table = Table(data, colWidths=[270,80,60,80,80])


    table.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ]))

    table.wrapOn(doc, width, height)
    table.drawOn(doc,10,10)

    doc.save()
    
    os.remove("num.txt") #Elimina ese archivo de numero

    f = open("num.txt","w") #Crea otro archio con el mismo numero
    f.write("{}".format(num+1)) #Escribo el numero del archivo anterior + 1
    f.close() #Cierra el numerp
