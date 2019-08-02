from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Table
from reportlab.lib import colors
from colorama import Fore, Back, Style
import math
import pandas as pd 
import locale
import csv
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

    def price(self,price):
        self._price = price
    def get_price(self):
        return self._price

    def print_all(self):
        print("     Desarollo = {}".format(self.get_des()))
        print("     Calibre = {}".format(self.get_cal()))
        print("     Piezas = {}".format(self.get_pcs()))
        print("     Numero de laminas = {}".format(self.get_lam()))
        print("     Tipo de lamina = {}".format(self.get_lam_type()))
        print("     Restante = {}".format(restante[len(restante)-1]))
        print("\n#####################################################################\n")  

class Tablon():
    def __init__(self,t_ancho,t_largo):
        self.set_ancho(t_ancho)
        self.set_largo(t_largo)

    def set_ancho(self,t_ancho):
        self._ancho = t_ancho
    def set_largo(self,t_largo):
        self._largo = t_largo

    def get_ancho(self):
        return self._t_ancho
    def get_largo(self):
        return self._t_largo

class Madera():
    def __init__(self,m_ancho,m_largo):
        self.set_ancho(m_ancho)
        self.set_largo(m_largo)

    def set_ancho(m_ancho):
        self._ancho = m_ancho
    def set_largo(m_largo):
        self._largo = m_largo

    def get_ancho(self):
        return self._m_ancho
    def get_largo(self):
        return self._m_largo

class Plafones():
    def __init__(self, precio):
        self.set_price(precio)

    def set_price(self,price):
        self._price = price

    def get_price(self):
        return self._price

def imprimir_cot(cop,cam,alto,ancho,largo,t_precio):

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

    #Plafones
    plafones4 = Plafones(149)
    plafones2 = Plafones(35)    

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
        
        data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
        row = data.loc[22]
        angulo.price(row[6])
        angulo.print_all()

    def p4x2(): #PTR 4X2    
        print("[8] PTR 4X2: ")
        tipo = "--"
        ptr4x2.lam_type(tipo)
        ptr4x2.add_pcs(1.5)

        data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
        row = data.loc[18] #Este es el id de cada material
        ptr4x2.price(row[6])   

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

        data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
        row = data.loc[17] #Este es el id de cada material
        ptr4x3.price(row[6])
        ptr4x3.add_pcs(parte_entera + parte_decimal)
        ptr4x3.print_all()

    def t15(): #TUBULAR 1 1/5
        print("[10] Tubular 1 1/2: ")
        tipo = "--"
        tubula.lam_type(tipo)
        t_piezas = ((((((estaca.get_pcs()-5)/2)+1)*(ancho/100))+14)/6)
        tubula.add_pcs(int(round(t_piezas)))

        data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
        row = data.loc[30] #Este es el id de cada material

        tubula.price(row[6])

        tubula.print_all()        

    def t1():  # [TUBULAR 1X1] [Incompleto]
        piezas = (((((ancho/2)*3)+(alto-10*3))*2)/600)*2
        tubula1x1.lam_type("--")
        tubula1x1.add_pcs(round(piezas))

        data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
        row = data.loc[29] #Este es el id de cada material
        tubula1x1.price(row[6])

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

    def t_piso():
        if t_precio == "normal":
            piso6x8 = Tablon(6,8)
            piso6x10 = Tablon(6,10)
            piso6x12 = Tablon(6,12)
            psio6x14 = Tablon(6,14)
            piso6x16 = Tablon(6,16)

            piso8x8 = Tablon(8,8)
            piso8x10 = Tablon(8,10)
            piso8x12 = Tablon(8,12)
            psio8x14 = Tablon(8,14)
            piso8x16 = Tablon(8,16)

        else:
            piso6x8 = Madera(6,8)
            piso6x10 = Madera(6,10)
            piso6x12 = Madera(6,12)
            psio6x14 = Madera(6,14)
            piso6x16 = Madera(6,16)

            piso8x8 = Madera(8,8)
            piso8x10 = Madera(8,10)
            piso8x12 = Madera(8,12)
            psio8x14 = Madera(8,14)
            piso8x16 = Madera(8,16)

    t_piso()

    lam_peso_total = (lamina3x10c12.get_lam()*lamina3x10c12.get_we()) + (lamina3x10c14.get_lam()*lamina3x10c14.get_we()) + (lamina3x8c12.get_lam()*lamina3x8c12.get_we()) + (lamina3x8c14.get_lam()*lamina3x8c14.get_we())
    lam_peso_total += (lamina4x10c12.get_lam()*lamina4x10c12.get_we()) + (lamina4x10c14.get_lam()*lamina4x10c14.get_we()) + (lamina4x8c12.get_lam()*lamina4x8c12.get_we()) + (lamina4x8c14.get_lam()*lamina4x8c14.get_we())

    laminas = [lamina4x10c14.get_lam(),lamina4x8c14.get_lam(),lamina3x10c14.get_lam(),lamina3x8c14.get_lam(),lamina4x10c12.get_lam(),lamina4x8c12.get_lam(),lamina3x10c12.get_lam(),lamina3x8c12.get_lam()]

    lam_precio_total = 0

    with open('C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        maxId = 0
        for row in csv_reader:
            if line_count != 0:
                #lam_precio_total += float(row[6])*float(laminas[i])
                if maxId < 8:
                    precio = row[6]
                    lam_precio_total += float(precio)*float(laminas[maxId])
                    maxId+=1
                else:
                    break
            else:
                line_count+=1


    for i in reversed(range(1,len(restante))):
        print("[!] [{}] [RESTANTES] {}".format(i,restante[i]))

    print("")   

    print_rest()

    # Funciones de la parte superior

    def camioneta_sin():
            titulo = "Carroceria para caja seca {} copete para {} ({})".format(cop,cam,t_precio).upper()

            f = open("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/num.txt","r+") #Abre el archivo lee el ultimo numero y lo guarad en una variable
            num = int(f.readline())
            f.close() #lo cierra

            doc_tittle ="({}) Carroceria para caja seca {} copete para {}.pdf".format(num,cop,cam)

            doc = canvas.Canvas(doc_tittle,pagesize=A4)
            doc.setFont('Helvetica-Bold',13)

            #Dibuja la carroceria
            #preserveAspectRatio=True
            doc.drawImage("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/dibujos/Sin título.png",0,350,preserveAspectRatio=True,width=600)

            doc.drawString(30,825,titulo) #Escribe el top del titulo

            '''
            Aquí se van a poner las funciones de cada troquelado
            '''

            Alto = 790

            doc.drawString(30,Alto,"MEDIDAS:") #Escribe las medidas 
            doc.drawString(30,Alto-20,"LARGO:")
            doc.drawString(30,Alto-40,"ANCHO:")
            doc.drawString(30,Alto-60,"ALTO:")
            
            doc.setFont('Helvetica-Bold',10)
            doc.drawString(95,Alto-20,"{} mts.".format(largo/100))
            doc.drawString(95,Alto-40,"{} mts.".format(ancho/100))
            doc.drawString(95,Alto-60,"{} mts.".format(alto/100))

            doc.drawString(190,Alto+4,"{}".format(tubula1x1.get_pcs()))

            doc.drawString(350,Alto-45,"{}".format(esquinero.get_pcs()))
            doc.drawString(325,Alto-63,"({}) {}".format(esquinero.get_lam(),esquinero.get_lam_type()))

            doc.drawString(130,Alto-147,"{}".format(portaluz.get_pcs()))
            doc.drawString(105,Alto-165,"({}) {}".format(portaluz.get_lam(),portaluz.get_lam_type()))

            doc.drawString(260,Alto-147,"{}".format(monten.get_pcs()))
            doc.drawString(235,Alto-165,"({}) {}".format(monten.get_lam(),monten.get_lam_type()))

            doc.drawString(390,Alto-147,"{}".format(lateral.get_pcs()))
            doc.drawString(365,Alto-165,"({}) {}".format(lateral.get_lam(),lateral.get_lam_type()))

            doc.drawString(550,Alto-147,"{}".format(estaca.get_pcs()))
            doc.drawString(525,Alto-165,"({}) {}".format(estaca.get_lam(),estaca.get_lam_type()))

            doc.drawString(150,Alto-256,"{}".format(casquillo.get_pcs()))
            doc.drawString(125,Alto-274,"({}) {}".format(casquillo.get_lam(),casquillo.get_lam_type()))

            doc.drawString(280,Alto-259,"{}".format(angulo.get_pcs()))

            doc.drawString(350,Alto-305,"{}".format(ptr4x3.get_pcs()))

            doc.drawString(440,Alto-305,"{}".format(ptr4x2.get_pcs()))

            doc.drawString(530,Alto-295,"{}".format(tubula.get_pcs()))

            locale.setlocale( locale.LC_ALL, '' )

            data = pd.read_csv("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/datos.csv")
            row = data.loc[65] #Este es el id de cada material
            toldo_precio = float(row[6])

            polin8 = largo/243.84
            print("largo / 243.84 = {}".format(polin8))
            parte_decimal_p8, parte_entera_p8 = math.modf(polin8)
            print("P8D: {} | P8E: {}".format(parte_decimal_p8,parte_entera_p8))
            polin16 = largo/487.68
            print("largo / 487.68 = {}".format(polin16))
            parte_decimal_p16, parte_entera_p16 = math.modf(polin16)
            print("P16D: {} | P16E: {}".format(parte_decimal_p16,parte_entera_p16))
            

            if parte_entera_p8 < parte_entera_p16 and parte_decimal_p8 < parte_decimal_p16:
                polin = "3x3x8"
                p_precio = 75
                p_usar = polin8
                print("P = {}\n PP = {}\nPU = {}".format(polin,p_precio,p_usar))
            elif parte_entera_p8 < parte_entera_p16 and parte_decimal_p8 > parte_decimal_p16:
                polin = "3x3x8"
                p_precio = 75
                p_usar = polin8
                print("P = {}\n PP = {}\nPU = {}".format(polin,p_precio,p_usar))
            elif parte_entera_p8 > parte_entera_p16 and parte_decimal_p8 > parte_decimal_p16:
                polin = "3x3x16"
                p_precio = 85
                p_usar = polin16
                print("P = {}\n PP = {}\nPU = {}".format(polin,p_precio,p_usar))
            elif parte_entera_p8 > parte_entera_p16 and parte_decimal_p8 < parte_decimal_p16:
                polin = "3x3x16"
                p_precio = 85
                p_usar = polin16
                print("P = {}\n PP = {}\nPU = {}".format(polin,p_precio,p_usar))
            else:
                messagebox.showerror("Erro","Impossible.")
            
            tot = [lam_precio_total,lam_peso_total*4.06,float(ptr4x2.get_pcs())*float(ptr4x2.get_price()),float(tubula1x1.get_pcs())*float(tubula1x1.get_price()),float(tubula.get_pcs())*float(tubula.get_price()),float(toldo_precio)*float((largo + 50)/100),float(angulo.get_pcs())*float(angulo.get_price()),((round((largo/122)*3)*295)),(plafones4.get_price()*6),((plafones2.get_price()*(((largo/100)-1)*2)+4)),((((largo/100)-1)*2)*110),2500,math.ceil(p_usar*2)*p_precio,1560]
            total = 0

            for i in range(0,len(tot)):
                total += tot[i]

            print(len(tot))
            data = [
                ["                                       MATERIAL","   CANTIDAD","  UNIDAD","     PRECIO","    TOTALES"],
                ["Material con lamina y maquila de varios calibres.","{} KG.".format(lam_peso_total)," ","","{}".format(locale.currency(math.ceil(tot[0]),grouping=True))],
                ["Maquila.",lam_peso_total,"","$ 4.06","{}".format(locale.currency(math.ceil(tot[1]),grouping=True))],
                ["PTR 4x2.",ptr4x2.get_pcs(),"","{}".format(locale.currency(float(ptr4x2.get_price()),grouping=True)),"{}".format(locale.currency(math.ceil(tot[2]),grouping=True))],
                ["Tubula 1''x1''. ",tubula1x1.get_pcs(),"","{}".format(locale.currency(float(tubula1x1.get_price()),grouping=True)),"{}".format(locale.currency(math.ceil(tot[3]),grouping=True))],
                ["Tubula 1 ½x 1 ½.",tubula.get_pcs(),"","{}".format(locale.currency(float(tubula.get_price()),grouping=True)),"{}".format(locale.currency(math.ceil(tot[4]),grouping=True))],
                ["Lamina aluminio (toldo).","260x{}".format(float(largo) + 50),"","{}".format(locale.currency(toldo_precio,grouping=True)),"{}".format(locale.currency(math.ceil(tot[5]),grouping=True))],
                ["Angulo",angulo.get_pcs(),"","{}".format(locale.currency(float(angulo.get_price()),grouping=True)),"{}".format(locale.currency(math.ceil(tot[6]),grouping=True))],
                # [COMPLETAR]
                ["Madera piso .","","","",""], 
                # [COMPLETAR]
                ["Triplay 6mm.",round((largo/122)*3),"","{}".format(locale.currency(295)),"{}".format(locale.currency(tot[7],grouping=True))],
                ["Plafones 4'' led.",6,"","{}".format(locale.currency(plafones4.get_price(),grouping=True)),"{}".format(locale.currency(tot[8],grouping=True))],
                ["[!] Plafones 2'' led. [!]","{}".format((largo/100)-1),"","{}".format(locale.currency(plafones2.get_price(),grouping=True)),"{} [!]".format(locale.currency(tot[9]/2,grouping=True))],
                ["Bragas 5/8.","{}".format(((largo/100)-1)*2),"","{}".format(locale.currency(110,grouping=True)),"{}".format(locale.currency(tot[10],grouping=True))],          
                ["Vistas.","","","","{}".format(locale.currency(tot[11],grouping=True))],
                ["Polin {}.".format(polin),"{}".format(math.ceil(p_usar*2)),"","{}".format(locale.currency(p_precio,grouping=True)),"{}".format(locale.currency((math.ceil(tot[12])),grouping=True))],   
                ["Bisagra y Pasadores.","4","","","{}".format(locale.currency(tot[13]))],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["Total","","","","{}".format(locale.currency(total,grouping=True))]
                ]

            table = Table(data, colWidths=[270,80,60,80,80])

            table.setStyle(TableStyle([
                                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                ]))

            table.wrapOn(doc, width, height)
            table.drawOn(doc,10,10)

            doc.save()
            
            os.remove("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/num.txt") #Elimina ese archivo de numero

            f = open("C:/Users/trabajo/Desktop/Cotizar/cotizar-1/num.txt","w") #Crea otro archio con el mismo numero
            f.write("{}".format(num+1)) #Escribo el numero del archivo anterior + 1
            f.close() #Cierra el archivo
            
            target = doc_tittle
            initial_dir = 'C:/Users/trabajo/Desktop/'

            path = ''
            for root, _, files in os.walk(initial_dir):
                if target in files:
                    path = os.path.join(root, target)
                    break

            if messagebox.askyesno("Atención","Se ah cotizado una carroceria para caja seca {} copete para {} de {}mts. de alto, {}mts. de ancho y {}mts. de largo. \n ¿Desea abrirla?".format(cop,cam,alto/100,ancho/100,largo/100)):
                os.popen(doc_tittle)

    def camioneta_con():
        pass

    def camion_sin():
        pass

    def camion_con():
        pass

    # -------------  HASTA AQUI ACDABAN LOS TROQUELADOS

    if cam == "camioneta":  
        if cop == "sin":
            camioneta_sin()
        else:
            camioneta_con()
    else:
        if cop == "sin":
            camion_sin()
        else:
            camion_con()

    def final():
        pass