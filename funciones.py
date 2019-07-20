from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table
from reportlab.lib import colors
import os

width,height = A4

class Material():
    def set_des(self,des):
        self._des = des
    def set_cal(self,cal):
        self._cal = cal

    def get_des(self):
        return self._des
    def get_cal(self):
        return self._cal

    def __init__(self,des,cal):
        set_des(des)
        set_cal(cal)
        self._pcs = 0
    
    def add_pcs(self,pcs):
        self._pcs += pcs
    def get_pcs(self):
        return self._pcs

    class Lamina():
        def set_alto(self,alto):
            self._alto = alto
        def set_ancho(self,ancho):
            self._ancho = ancho
        def set_we(self,we): #!
            self._we = we

        def get_alto(self):
            return self._alto
        def get_ancho(self):
            return self._ancho
        def get_we(self): #!
            return self._we

        def __init__(self,alto,ancho,we):
            set_alto(alto)
            set_ancho(ancho)
            set_we(we) #!
            self._lam = 0

        def add_lam(self,lam):
            self._lam+=lam
        def get_lam(self):
            return self._lam

def imprimir_cot(cop,cam,alto,ancho,largo):

    esquinero = Material(32,14)
    portaluz = Material(54.5,14)
    mouter = Material(17.3,12)
    lateral = Material(28,14)
    estaca = Material(15.2,14)
    casquillo = Material(20.5,14)
    angulo = Material(0,"3/6 x 2")
    ptr4x2 = Material(0,11)
    ptr4x3 = Material(0,11)
    ptr = Material(0,18) #PTR 1 1/2 x 1 1/2
    tubula = Material(0,8) #TUBULA 1 1/2 x 1 1/2
    tubula1x1 = Material(0,18)

    # Lamina cal 14
    lamina4x10c14 = Material()
    lamina4x10c14.Lamina(122,305,57)
    lamina4x8c14 = Material()
    lamina4x8c14.Lamina(122,244,46)
    lamina3x10c14 = Material()
    lamina3x10c14.Lamina(91.5,305,43)
    lamina3x8c14 = Material()
    lamina3x8c14.Lamina(91.5,244,35)

    # Lamina cal 12
    lamina4x10c12 = Material()
    lamina4x10c12.Lamina(122,305,80)
    lamina4x8c12 = Material()
    lamina4x8c12.Lamina(122,244,64)
    lamina3x10c12 = Material()
    lamina3x10c12.Lamina(91.5,305,60)
    lamina3x8c12 = Material()
    lamina3x8c12.Lamina(91.5,244,48)

    if cam == "camioneta":
        titulo = "Carroceria para caja seca {} copete para {}".format(cop,cam).upper()

        f = open("num.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
        num = int(f.readline())
        print("Numero leido: {}".format(num))
        f.close() #lo cierra

        doc_tittle ="({}) Carroceria para caja seca {} copete para {}.pdf".format(num,cop,cam)

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
        initial_dir = 'C:/Users/trabajo/Desktop/'

        path = ''
        for root, _, files in os.walk(initial_dir):
            if target in files:
                path = os.path.join(root, target)
                break

        print("PDF encontrado")

        if messagebox.askyesno("Atención","Se ah cotizado una carroceria para caja seca {} copete para {} de {}mts. de alto, {}mts. de ancho y {}mts. de largo. \n ¿Desea abrirla?".format(cop,cam,alto,ancho,largo)):
            os.popen(doc_tittle)
    else:
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
        initial_dir = 'C:/Users/trabajo/Desktop/'

        path = ''
        for root, _, files in os.walk(initial_dir):
            if target in files:
                path = os.path.join(root, target)
                break

        print("PDF encontrado")

        if messagebox.askyesno("Atención","Se ah cotizado una carroceria para caja seca {} copete para {} de {}mts. de alto, {}mts. de ancho y {}mts. de largo. \n ¿Desea abrirla?".format(cop,cam,alto,ancho,largo)):
            os.popen(doc_tittle)