from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table
from reportlab.lib import colors
from colorama import Fore, Back, Style
import math
import os

width,height = A4

class Lamina():
        def __init__(self,ancho,largo,we):
            self.set_ancho(ancho)
            self.set_largo(largo)
            self.set_we(we) #!
            self._lam = 0

        def set_largo(self,largo):
            self._largo = largo
        def set_ancho(self,ancho): #Estas nunca mas se van a ejecutar while running
            self._ancho = ancho
        def set_we(self,we): #!
            self._we = we

        def get_largo(self):
            return self._largo
        def get_ancho(self):
            return self._ancho #Estas si
        def get_we(self): #!
            return self._we

        def add_lam(self,lam):
            self._lam+=lam
        def get_lam(self):  #Y esta
            return self._lam

class Material():

    def __init__(self,des,cal):
        self.set_des(des)
        self.set_cal(cal)
        self._pcs = 0
        self._lam = 0

    def set_des(self,des):
        self._des = des
    def set_cal(self,cal):
        self._cal = cal   

    def get_des(self):
        return self._des
    def get_cal(self):
        return self._cal
    
    def add_pcs(self,pcs):
        self._pcs += pcs
    def get_pcs(self):
        return self._pcs

    def lam_can(self,lam):
        self._lam = lam
    def lam_type(self,lam_type):
        self._lam_type = lam_type

    def get_lam(self):
        return self._lam
    def get_lam_type(self):
        return self._lam_type

    def print_all(self):
        print("     Desarollo = {}".format(self.get_des()))
        print("     Calibre = {}".format(self.get_cal()))
        print("     Piezas = {}".format(self.get_pcs()))
        print("     Numero de laminas = {}".format(self.get_lam()))
        print("     Tipo de lamina = {}".format(self.get_lam_type()))
        print("\n#####################################################################\n")

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
    lamina4x10c14 = Lamina(122,305,57)
    lamina4x8c14 = Lamina(122,244,46)
    lamina3x10c14 = Lamina(91.5,305,43)
    lamina3x8c14 = Lamina(91.5,244,35)

    # Lamina cal 12
    lamina4x10c12 = Lamina(122,305,80)
    lamina4x8c12 = Lamina(122,244,64)
    lamina3x10c12 = Lamina(91.5,305,60)
    lamina3x8c12 = Lamina(91.5,244,48)

    restante = []

    os.system("cls")

    def esquina():  #Esquinero [Siempre]
        print("Esquinero :")
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo3x8 = "3x8"    

        esquinero.add_pcs(2)
        laminas += 1
        lamina3x10c14.add_lam(laminas)
        esquinero.lam_can(laminas)
        esquinero.lam_type(tipo3x8)
        lamina3x8c14.add_lam(laminas)
        restante.append(lamina3x10c14.get_ancho()-(esquinero.get_pcs()*esquinero.get_des()))
        print("[1]")
        esquinero.print_all()

    def portluz():   #Portaluz
        print("Portaluz: ")   
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo3x10 = "3x10"
        no_piezas = lamina4x10c14.get_ancho() / portaluz.get_des()
        px2 = lamina3x10c14.get_ancho() / portaluz.get_des()
        portaluz.lam_can(1)

        if no_piezas<px2:
            portaluz.add_pcs(int(no_piezas))
            portaluz.lam_type(tipo4x10)
            lamina4x10c14.add_lam(1)
            restante.append(lamina4x10c14.get_ancho()-(portaluz.get_pcs()*portaluz.get_des()))
            print("[2-1]")
            
        else:
            portaluz.add_pcs(int(px2))
            portaluz.lam_type(tipo3x10)
            lamina3x10c14.add_lam(1)
            restante.append(lamina3x10c14.get_ancho()-(portaluz.get_pcs()*portaluz.get_des()))
            print("[2-2]")

        portaluz.print_all()

    def mou(): #Mouter
        print("Mouter: ")
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo4x8 = "4x8"
        print("[ ! (3) !]")
        no_laminas = float(largo) / int(lamina4x8c14.get_largo())
        no_piezas = (lamina4x8c14.get_ancho()*round(no_laminas)) / mouter.get_des()
        mouter.add_pcs((round(no_piezas)))
        mouter.lam_can(round(no_laminas))
        mouter.lam_type(tipo4x8)
        lamina4x8c12.add_lam(no_laminas)
        mouter.print_all()

    def plata(): #Plataforma
        print("L. Plataforma: ")
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo3x10 = "3x10"
        print("[4]")
        l = 0
        lamas4x10 = 0
        lamas4x8 = 0
        # Debuggin [!]
        while l < largo*2:
            if l + 305 <= largo*2:
            #  print("[!] {} + 244 ({}) <<< {}".format(l,l+244,largo*2))
            #   print("{} + 305 ({}) <= {}".format(l,l+305,largo*2))
                l += 305
                lamas4x10 += 1  
            #    print("L4x10 + 1 ({})".format(lamas4x10))
            elif l + 244 <= largo:
        #         print("[!] {} + 305 ({}) >>> {}".format(l,l+305,largo*2))
        #          print("{} + 244 ({}) <= {}".format(l,l+244,largo*2))
                    l += 244
                    lamas4x8 += 1
        #           print("L8x10 + 1 ({})".format(lamas4x8))
            else:
                break

        # Debuggin [!]
        lateral.add_pcs(lamas4x10 + lamas4x8)
        total = lamas4x10 + lamas4x8 
        lateral.lam_can(total)
        lateral.lam_type("--")
        lamina4x10c14.add_lam(lamas4x10)
        lamina4x8c14.add_lam(lamas4x8)
        lateral.print_all()
        restante.append(lamina4x10c14.get_ancho()-(lateral.get_pcs()*lateral.get_des()))

    def es():# Estaca
        print("Estaca : ")
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo3x10 = "3x10"
        
        no_laminas = largo / 244
        no_laminas1 = int(no_laminas*2)
        piezas = (122*no_laminas1) / estaca.get_des()
        estaca.add_pcs(int(piezas))
        estaca.lam_can(no_laminas1)
        estaca.lam_type(tipo4x10)
        lamina4x10c14.add_lam(no_laminas)
        restante.append(lamina4x10c14.get_ancho()*estaca.get_lam()-(estaca.get_pcs()*estaca.get_des()))
        if int(restante[3]) != restante[3]: 
            estaca.add_pcs(1)
        else:
            estaca.add_pcs(-1)
        estaca.print_all()

    def casq():
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo3x10 = "3x10"
        
    esquina()
    portluz()
    mou()
    plata() 
    es()    

    for i in reversed(range(0,len(restante))):
        print("[!] [{}] [RESTANTES] {}".format(i,restante[i]))

    print("\n")

    if lamina3x10c12.get_lam() != 0:
        print(u"[\u23C3 ] 3x10 c12 = {}".format(lamina3x10c12.get_lam()))
    if lamina3x10c14.get_lam() != 0:
        print(u"[\u23C3 ] 3x10 c14 = {}".format(lamina3x10c14.get_lam()))
    if lamina3x8c12.get_lam() != 0:
        print(u"[\u23C3 ] 3x8 c12 = {}".format(lamina3x8c12.get_lam()))
    if lamina3x8c14.get_lam() != 0:
        print(u"[\u23C3 ] 3x8 c14 = {}".format(lamina3x8c14.get_lam()))
    if lamina4x10c12.get_lam() != 0:
        print(u"[\u23C3 ] 4x10 c12 = {}".format(lamina4x10c12.get_lam()))
    if lamina4x10c14.get_lam() != 0:
        print(u"[\u23C3 ] 4x10 c14 = {}".format(lamina4x10c14.get_lam()))
    if lamina4x8c12.get_lam() != 0:
        print(u"[\u23C3 ] 4x8 c12 = {}".format(lamina4x8c12.get_lam()))
    if lamina4x8c14.get_lam() != 0:
        print(u"[\u23C3 ] 4x8 c14 = {}".format(lamina4x8c14.get_lam()))

    # -------------  HASTA AQUI ACDABAN LOS TROQUELADOS

    if cam == "camioneta":  
        titulo = "Carroceria para caja seca {} copete para {}".format(cop,cam).upper()

        f = open("num.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
        num = int(f.readline())
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
        
        target = doc_tittle
        initial_dir = 'C:/Users/trabajo/Desktop/'

        path = ''
        for root, _, files in os.walk(initial_dir):
            if target in files:
                path = os.path.join(root, target)
                break

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