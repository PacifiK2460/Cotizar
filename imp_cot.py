from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
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

def main():

    f = open("cop.txt","r") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    cop = f.readline("cop.txt")
    f.close() #lo cierra

    f = open("cam.txt","r") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    cam = f.readline("cam.txt")
    f.close() #lo cierra

    f = open("alto.txt","r") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    alto = f.readline("alto.txt")
    f.close() #lo cierra

    f = open("ancho.txt","r") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    ancho = f.readline("ancho.txt")
    f.close() #lo cierra

    f = open("largo.txt","r") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    largo = f.readline("largo.txt")
    f.close() #lo cierra

    titulo = "Carroceria para caja seca {} copete para {}".format(cop,cam).upper()

    f = open("num.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
    num = int(f.readline())
    print("Numero leido: {}".format(num))
    f.close() #lo cierra

    doc_tittle ="Carroceria para caja seca {} copete para {} ({}).pdf".format(cop,cam,num)

    doc = canvas.Canvas(doc_tittle,pagesize=A4)
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
    f.close() #Cierra el archivo

    print("Buscando pdf...")
    
    target = doc_tittle
    initial_dir = 'C:/Users/trabajo/'

    path = ''
    for root, _, files in os.walk(initial_dir):
        if target in files:
            path = os.path.join(root, target)
            break

    print("PDF encontrado")

    messagebox.showinfo("Atención","Se ah cotizado una carroceria para caja seca {} copete para {} de {}mts. de alto, {}mts. de ancho y {}mts. de largo.".format(cop,cam,alto,ancho,largo))

main()