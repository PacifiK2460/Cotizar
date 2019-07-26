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

restante = []

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
        print("     Restante = {}".format(restante[len(restante)-1]))
        print("\n#####################################################################\n")


def imprimir_cot(cop,cam,alto,ancho,largo):
    esquinero = Material(32,14)
    portaluz = Material(54.5,14)
    monten = Material(17.3,12)
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

    os.system("cls")

    def print_rest():
        if lamina3x10c12.get_lam() != 0:
            print("[!] [Info] 3x10 c12 = {}".format(lamina3x10c12.get_lam()))
        if lamina3x10c14.get_lam() != 0:
            print("[!] [Info] 3x10 c14 = {}".format(lamina3x10c14.get_lam()))
        if lamina3x8c12.get_lam() != 0:
            print("[!] [Info] 3x8 c12 = {}".format(lamina3x8c12.get_lam()))
        if lamina3x8c14.get_lam() != 0:
            print("[!] [Info] 3x8 c14 = {}".format(lamina3x8c14.get_lam()))
        if lamina4x10c12.get_lam() != 0:
            print("[!] [Info] 4x10 c12 = {}".format(lamina4x10c12.get_lam()))
        if lamina4x10c14.get_lam() != 0:
            print("[!] [Info] 4x10 c14 = {}".format(lamina4x10c14.get_lam()))
        if lamina4x8c12.get_lam() != 0:
            print("[!] [Info] 4x8 c12 = {}".format(lamina4x8c12.get_lam()))
        if lamina4x8c14.get_lam() != 0:
            print("[!] [Info] 4x8 c14 = {}".format(lamina4x8c14.get_lam()))

    #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--

    def esquina(): #Esquinero [Siempre]
        print("[1] Esquinero :")
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
        esquinero.print_all()

    def portluz(): #Portaluz
        print("[2] Portaluz: ")   
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
        print("[3] Mouter: ")
        laminas = 0
        lam_name = ""
        tipo4x8 = "4x8"
        no_laminas = float(largo) / int(lamina4x8c14.get_largo())
        no_piezas = (lamina4x8c14.get_ancho()*round(no_laminas)) / monten.get_des()
        monten.add_pcs((round(no_piezas)))
        monten.lam_can(round(no_laminas))
        monten.lam_type(tipo4x8)
        lamina4x8c12.add_lam(round(no_laminas))
        monten.print_all()

    def plata(): #Plataforma
        print("[4] L. Plataforma: ")
        laminas = 0
        lam_name = ""
        tipo4x10 = "4x10"
        tipo3x10 = "3x10"
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
            elif l + 244 <= largo*2+244 and l+244 >=largo*2:
        #         print("[!] {} + 305 ({}) >>> {}".format(l,l+305,largo*2))
        #          print("{} + 244 ({}) <= {}".format(l,l+244,largo*2))
                    l += 244
                    lamas4x8 += 1
        #           print("L8x10 + 1 ({})".format(lamas4x8))
            else:
                break

        # Debuggin [!]
        lateral.add_pcs(lamas4x10)
        lateral.lam_can(1)
        lateral.lam_type("4x10")
        lamina4x10c14.add_lam(1)
        restante.append(lamina4x10c14.get_ancho()-(lateral.get_pcs()*lateral.get_des()))
        lateral.add_pcs(lamas4x8)
        lateral.print_all()

    def es():# Estaca
        print("[5] Estaca : ")
        laminas = 0
        lam_name = ""
        tipo4x8 = "4x8"
        
        no_laminas = largo / 244
        no_laminas1 = int(no_laminas*2)
        piezas = (122*no_laminas1) / estaca.get_des()
        estaca.add_pcs(int(piezas))
        estaca.lam_can(no_laminas1)
        estaca.lam_type(tipo4x8)
        lamina4x8c14.add_lam(no_laminas1)
        restante.append(lamina4x10c14.get_ancho()*estaca.get_lam()-(estaca.get_pcs()*estaca.get_des()))
        if int(restante[3]) != restante[3]: 
            estaca.add_pcs(1)
        else:
            estaca.add_pcs(-1)

        estaca.print_all()

    def casq(): #Casquillo
        print("[6] Casquillo: ")
        tipo3x10 = "3x10"

        casquillo.add_pcs(int((largo/3)*2/100))
        casquillo.lam_type(tipo3x10)
        casquillo.lam_can(1)
        casquillo.print_all()

    def ang(): #Angulo
        print("[7] Angulo: ")
        tipo = "--"
        angulo.lam_type(tipo)
        piezas = ((monten.get_pcs()*2)*19)/600
        parte_decimal, parte_entera = math.modf(piezas)
        if parte_decimal >= 0.1 and parte_decimal <= 0.5:
            parte_decimal = 0.5
        elif parte_decimal >= 0.6 and parte_decimal <= 0.9:
            parte_decimal = 0
            parte_entera += 1
        angulo.add_pcs(parte_entera + parte_decimal)
        angulo.print_all()

    def p4x2(): #PTR 4X2    
        print("[8] PTR 4X2: ")
        tipo = "--"
        ptr4x2.lam_type(tipo)
        ptr4x2.add_pcs(1.5)
        ptr4x2.print_all()

    def p4x3(): #PTR 4X3
        print("[9] PTR 4X3:   ")
        tipo = "--"
        ptr4x3.lam_type(tipo)
        piezas = largo*2/600
        parte_decimal, parte_entera = math.modf(piezas)
        if parte_decimal >= 0.1 and parte_decimal <= 0.5:
            parte_decimal = 0.5
        elif parte_decimal >= 0.6 and parte_decimal <= 0.9:
            parte_decimal = 0
            parte_entera += 1
        ptr4x3.add_pcs(parte_entera + parte_decimal)
        ptr4x3.print_all()

    def t15(): #TUBULAR 1 1/5
        print("[10] Tubular 1 1/2: ")
        tipo = "--"
        tubula.lam_type(tipo)
        t_piezas = ((((((estaca.get_pcs()-5)/2)+1)*(ancho/100))+14)/6)
        tubula.add_pcs(int(round(t_piezas)))
        tubula.print_all()        

    def t1():  # [TUBULAR 1X1] [Incompleto]
        piezas = (((((ancho/2)*3)+(alto-10*3))*2)/600)*2
        tubula1x1.lam_type("--")
        tubula1x1.add_pcs(round(piezas))
        tubula1x1.print_all()

    esquina()
    portluz()
    mou()
    plata() 
    es()
    casq()
    ang()
    p4x2()   
    p4x3()
    t15()
    t1()

    for i in reversed(range(1,len(restante))):
        print("[!] [{}] [RESTANTES] {}".format(i,restante[i]))

    print("")   

    print_rest()

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