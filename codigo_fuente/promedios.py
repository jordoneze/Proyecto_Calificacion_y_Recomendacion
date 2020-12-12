import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from urllib.request import urlopen

def vermaterias():
    print("Blue")


def agregaryaaproyectarnota(entrynot, entryporcen, notasaevaluar, porcentajesaevaluar):
    nota_proy=int(entryporcen.get())
    porcentaje=int(entrynot.get())
    notasaevaluar.append(nota_proy)
    porcentajesaevaluar.append(porcentaje)


def yaaproyectarnota(notasaevaluar, porcentajesaevaluar, total_porcentaje, nota_acumulada, etiquetaresul):
    for result in range(0, len(notasaevaluar)):
        total_porcentaje = total_porcentaje + porcentajesaevaluar[result]
        nota_acumulada = nota_acumulada + notasaevaluar[result] * (porcentajesaevaluar[result] / 100)
    porcentaje_residuo = (100 - total_porcentaje) / 100
    nota_necesaria = (3.0 - nota_acumulada) / porcentaje_residuo

    etiquetaresul.configure(text="Debes obtener "+str(round(nota_necesaria,1)))
    etiquetaresul.place(x=460, y=470, heigh=26)


def ocultaragregarmaterias(entrymat, entrycodig, entrynota,entrycredit,entryaprueb,entrysemestre):
    ocultar_bl(entrymat)
    ocultar_bl(entrycodig)
    ocultar_bl(entrynota)
    ocultar_bl(entrycredit)
    ocultar_bl(entryaprueb)
    ocultar_bl(entrysemestre)

def ahoraagregar(entrymat, entrycodig, entrynota,entrycredit,entryaprueb,entrysemestre, nombreusu):
    nommat=entrymat.get()
    codigom=entrycodig.get()
    notam=entrynota.get()
    creditosm=entrycredit.get()
    aprueb=entryaprueb.get()
    semestrem=entrysemestre.get()

    try:
        z = open('Usuarios.txt', 'r')
        inform=z.read()
        informlist = inform.split("\n")
        for persona in range(0, len(informlist)):
            informlist[persona] = informlist[persona].split("$%")
        z.close()
        for persona in range(0, len(informlist)):
            if informlist[0] ==nombreusu:
                print("boo")
    except:
        print("Boo2")



def agregarmaterias(entrymat, entrycodig, entrynota,entrycredit,entryaprueb,entrysemestre, etiquetaprom, etiquetaaprub,etiquetacod,etiquetacredit, etiquetanota, etiquetasemestre):

    etiquetaprom.place(x=420, y=220, heigh=26)
    etiquetaaprub.place(x=420, y=420, heigh=26)
    etiquetacod.place(x=420, y=270, heigh=26)
    etiquetacredit.place(x=420, y=370, heigh=26)
    etiquetanota.place(x=420, y=320, heigh=26)
    etiquetasemestre.place(x=420, y=470, heigh=26)



    entrymat.place(x=590, y=220, heigh=26)
    entrycodig.place(x=590, y=270, heigh=26)
    entrynota.place(x=590, y=320, heigh=26)
    entrycredit.place(x=590, y=370, heigh=26)
    entryaprueb.place(x=590, y=420, heigh=26)
    entrysemestre.place(x=590, y=470, heigh=26)




def seccion_materias(window, nombreusu, boton_vermat, boton_agremat):

    boton_vermat.place(x=510, y=200)
    boton_agremat.place(x=510, y=250)



def seccion_proyectar(window, nombreusu, boton_agregar, boton_listoag, entrynot, entryporcen, etiquetanotaa,etiquetaporcentaje ):

    boton_agregar.place(x=510, y=230)

    boton_listoag.place(x=510, y=280)

    entrynot.place(x=512, y=180, heigh=26)
    entryporcen.place(x=512, y=130, heigh=26)
    etiquetanotaa.place(x=345, y=130, heigh=26)
    etiquetaporcentaje.place(x=345, y=180, heigh=26)



def seccion_calcular(window,boton_PA,boton_PAPA, boton_PAPPI,  nombreusu):

    boton_PA.place(x=510, y=200)

    boton_PAPA.place(x=510, y=250)


    boton_PAPPI.place(x=510, y=300)



def accedido(window, nombreusu):
    notasaevaluar=[]
    nota_acumulada = 0
    porcentajesaevaluar = []
    total_porcentaje = 0

    etiquetaresul=tk.Label(window, font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=26)

    boton_calc = tk.Button(window, text="Calcular", bg=_from_rgb((148, 180, 59)), fg="white", width=15, height=1,
                           font=("Adobe Garamond Pro", 12))

    boton_mat = tk.Button(window, text="Materias", bg=_from_rgb((148, 180, 59)), fg="white", width=15, height=1,
                          font=("Adobe Garamond Pro", 12))

    boton_proynot = tk.Button(window, text="Proyectar Notas", bg=_from_rgb((148, 180, 59)), fg="white", width=15,
                              height=1,
                              font=("Adobe Garamond Pro", 12))

    boton_PA = tk.Button(window, text="PA", bg=_from_rgb((70, 107, 63)), fg="white", width=15, height=1,
                         font=("Adobe Garamond Pro", 18))

    boton_PAPA = tk.Button(window, text="PAPA", bg=_from_rgb((70, 107, 63)), fg="white", width=15,
                           height=1,
                           font=("Adobe Garamond Pro", 18))

    boton_PAPPI = tk.Button(window, text="PAPPI", bg=_from_rgb((70, 107, 63)), fg="white", width=15,
                            height=1,
                            font=("Adobe Garamond Pro", 18))

    boton_agregar = tk.Button(window, text="Agregar nota", bg=_from_rgb((70, 107, 63)), fg="white", width=15, height=1,
                           font=("Adobe Garamond Pro", 18))

    boton_listoag = tk.Button(window, text="Proyectar", bg=_from_rgb((70, 107, 63)), fg="white", width=15,
                             height=1,
                             font=("Adobe Garamond Pro", 18))

    entrynot = ttk.Entry(window, width=35)

    entryporcen = ttk.Entry(window, width=35)


    boton_vermat = tk.Button(window, text="Visualizar materias", bg=_from_rgb((70, 107, 63)), fg="white", width=15, height=1,
                           font=("Adobe Garamond Pro", 18))

    boton_agremat = tk.Button(window, text="Agregar materias", bg=_from_rgb((70, 107, 63)), fg="white", width=15,
                             height=1,
                             font=("Adobe Garamond Pro", 18))

    etiquetanomb = tk.Label(window, text="Materia",
                            font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")
    etiquetacod = tk.Label(window, text="Codigo",
                            font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")
    etiquetanota = tk.Label(window, text="Nota",
                            font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")
    etiquetacredit = tk.Label(window, text="Creditos",
                            font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")
    etiquetaaprub = tk.Label(window, text="Aprueba o no",
                            font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")
    etiquetasemestre = tk.Label(window, text="Semestre",
                            font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")



    etiquetanotaa = tk.Label(window, text="Nota",
                             font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")
    etiquetaporcentaje = tk.Label(window, text="Porcentaje",
                                  font=("Adobe Garamond Pro", 16), bg=_from_rgb((177, 178, 176)), width=13, anchor="e")

    entrymat = ttk.Entry(window, width=35)
    entrycodig = ttk.Entry(window, width=35)
    entrynota = ttk.Entry(window, width=35)
    entrycredit = ttk.Entry(window, width=35)
    entryaprueb = ttk.Entry(window, width=35)
    entrysemestre = ttk.Entry(window, width=35)



    boton_mat.place(x=310, y=20)

    boton_proynot.place(x=455, y=20)

    boton_calc.place(x=600, y=20)

    boton_cerrar_sesion = tk.Button(window, text="Cerrar Sesion", bg=_from_rgb((70, 107, 63)), fg="white", width=15,
                              height=1,
                              font=("Adobe Garamond Pro", 12))

    boton_cerrar_sesion.place(x=910, y=20)

    boton_cerrar_sesion.configure(command=lambda:[pantalla_principal(window),ocultar_bl(boton_PA), ocultar_bl(boton_PAPA),ocultar_bl(boton_PAPPI), ocultar_bl(entrynot), ocultar_bl(entryporcen),ocultar_bl(boton_agregar), ocultar_bl(boton_listoag), ocultar_bl(boton_vermat),ocultar_bl(boton_agremat), ocultar_bl(boton_proynot), ocultar_bl(boton_mat), ocultar_bl(boton_calc), ocultar_bl(boton_cerrar_sesion)])

    boton_mat.configure(command=lambda:[seccion_materias(window, nombreusu, boton_vermat, boton_agremat),ocultar_bl(boton_PA), ocultar_bl(boton_PAPA),ocultar_bl(boton_PAPPI), ocultar_bl(entrynot), ocultar_bl(entryporcen),ocultar_bl(boton_agregar), ocultar_bl(boton_listoag),  ocultar_bl(etiquetaporcentaje), ocultar_bl(etiquetanotaa)])
    boton_proynot.configure(command=lambda:[seccion_proyectar(window, nombreusu, boton_agregar, boton_listoag, entrynot, entryporcen, etiquetanotaa,etiquetaporcentaje ),ocultar_bl(boton_PA), ocultar_bl(boton_PAPA),ocultar_bl(boton_PAPPI), ocultar_bl(boton_vermat),ocultar_bl(boton_agremat)])
    boton_calc.configure(command=lambda:[seccion_calcular(window,boton_PA,boton_PAPA, boton_PAPPI,  nombreusu), ocultar_bl(boton_agregar), ocultar_bl(boton_listoag), ocultar_bl(entrynot), ocultar_bl(entryporcen), ocultar_bl(boton_vermat),ocultar_bl(boton_agremat), ocultar_bl(etiquetaporcentaje), ocultar_bl(etiquetanotaa)])

    boton_vermat.configure(command=lambda:[])
    boton_agremat.configure(command=lambda:[agregarmaterias(entrymat, entrycodig, entrynota,entrycredit,entryaprueb,entrysemestre, etiquetanomb, etiquetaaprub,etiquetacod,etiquetacredit, etiquetanota, etiquetasemestre), ocultar_bl(boton_vermat),ocultar_bl(boton_agremat)])

    boton_agregar.configure(command=lambda:[agregaryaaproyectarnota(entrynot, entryporcen, notasaevaluar, porcentajesaevaluar)])

    boton_listoag.configure(command=lambda:[(yaaproyectarnota(notasaevaluar, porcentajesaevaluar, total_porcentaje, nota_acumulada, etiquetaresul))])



def acceder(window,entrycont, entry3,boton_prom,boton_papapapi, boton_iniciarses, etiqueta2, etiquetacontra, boton_regresaracced, boton_acceder):
    nombreusu = entry3.get()
    contrasenia = entrycont.get()
    usuarios=leer_usuarios()
    for persona in usuarios:
        if nombreusu == persona[2]:
            if contrasenia == persona[3]:
                ret_acceder = "True"
                print("adentro")
                accedido(window, nombreusu)
                ocultar_bl(boton_iniciarses)
                ocultar_bl(entrycont)
                ocultar_bl(entry3)
                ocultar_bl(etiqueta2)
                ocultar_bl(etiquetacontra)
                ocultar_bl(boton_regresaracced)
                ocultar_bl(boton_acceder)
                ocultar_bl(boton_papapapi)
                ocultar_bl(boton_prom)
                ocultar_bl(boton_iniciarses)

                return
            else:
                print("Intente de nuevo")
                menu_acceder(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses)
    print("Usuario invalido")
    menu_acceder(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses)


def leer_usuarios():
    try:
        f = open('Usuarios.txt', 'r')
        mensaje = f.read()
        mensajelist=mensaje.split("\n%")
        for persona in range(0,len(mensajelist)):
            mensajelist[persona]= mensajelist[persona].split("\n")

        f.close()
        print(mensajelist)
        return mensajelist
    except:
        f = open('Usuarios.txt', 'w')
        f.close()
        leer_usuarios()


def webscrapingsae():
    url = "http://www.sae.unal.edu.co/promedios/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '' ]
    for linea in lineas:
        if linea[0]=="P" and linea[-1]==".":
            infoimport=linea
    return infoimport

def wikisoyunal():
    listagood=[]
    url = "https://tambinsoyunal.fandom.com/es/wiki/PAPA"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '' ]
    for linea in lineas:
        linea.strip()
        if linea[0]==" " and linea[-1]==".":
            for posi in range(0, len(linea) - 4):
                if linea[posi:posi + 4] == "El P":
                    sale = linea[posi:]
                    listagood.append(sale)

                    break
            break
    for linea in range(0,len(lineas)):
        if lineas[linea]=="Cálculo del PAPA":
            newlist=[lineas[linea],lineas[linea+1],lineas[linea+2],lineas[linea+3], lineas[linea+4], lineas[linea+5], lineas[linea+6], lineas[linea+7]]
            listagood.append(newlist)

        elif lineas[linea]=="Relación entre PAPA y PA":
            newlist = [lineas[linea], lineas[linea + 1], lineas[linea + 2]]
            listagood.append(newlist)

        elif lineas[linea]=="Implicaciones a los estudiantes":
            newlist = lineas[linea:linea+15]
            listagood.append(newlist)

        elif lineas[linea]=="Se podría clasificar a un estudiante según los siguientes criterios:":
            newlist = lineas[linea+1:linea + 9]
            listagood.append(newlist)

        elif lineas[linea]==" PAPPI ":
            newlist = lineas[linea:linea + 6]
            listagood.append(newlist)

    return listagood

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def ocultar_bl(boton):

    boton.place_forget()



def init_window():
    window = tk.Tk()
    window.title("Proyecto")
    window.geometry("1200x700")

    window.configure(bg=_from_rgb((177, 178, 176)))
    pruebainicses=False
    pantalla_principal(window,pruebainicses)

    window.mainloop()


def pantalla_principal(window, pruebainicses=False, nombreusu=""):



    salida=webscrapingsae()
    boton_prom = tk.Button(window, text="Promedios", bg=_from_rgb((148, 180, 59)), fg="white", width=15, height=1,
                              font=("Adobe Garamond Pro", 12))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_prom.place(x=20, y=20)

    boton_papapapi = tk.Button(window, text="PAPA-PA-PAPPI", bg=_from_rgb((148, 180, 59)), fg="white", width=15, height=1,
                           font=("Adobe Garamond Pro", 12))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_papapapi.place(x=165, y=20)



    boton_iniciarses = tk.Button(window, text="Iniciar sesión", bg=_from_rgb((166, 28, 49)), fg="white", width=15,
                               height=1,
                               font=("Adobe Garamond Pro", 12))
    """Para la funcion agregar command tras una coma = y la funcion"""
    if pruebainicses==False:
        boton_iniciarses.place(x=1035, y=20)
        pruebainicses = False
    else:
        pruebainicses=True



    etiquetaprom = tk.Label(window, text="Promedios", font=("Adobe Garamond Pro Bold", 20))  # Etiqueta de titulo de promedios
    etiquetaprom.place(x=80, y=70)
    etiquetaprom.configure(bg=_from_rgb((177, 178, 176)))

    texto = tk.Label(window, wraplength=500,text=salida,
                            font=("Adobe Garamond Pro", 12))  # Etiqueta de titulo de promedios
    texto.place(x=70, y=140)
    texto.configure(bg=_from_rgb((177, 178, 176)), width=100, anchor="w")

    img = Image.open('promedy.gif')
    image_logo = ImageTk.PhotoImage(img)
    widget = tk.Label(window, image=image_logo)
    widget.place(x=700, y=140) # La imagen no se ve puesto que se presenta un error al tenerla dentro de una funcion

    boton_papapapi.configure(command=lambda: [ocultar_bl(widget), ocultar_bl(texto), ocultar_bl(etiquetaprom), funcion_papapapappi(window, boton_prom,boton_iniciarses, boton_papapapi, pruebainicses)])
    boton_iniciarses.configure(command=lambda:[pantalla_principal2(window, boton_prom,boton_papapapi,boton_iniciarses, pruebainicses),ocultar_bl(widget), ocultar_bl(texto), ocultar_bl(etiquetaprom)])


    #boton_prom.configure(command=lambda: [ocultar_boton_crear(boton_crear_cuenta),
                                             #ocultar_boton_acceder(boton_acceder),
                                             #ocultar_etiqueta_bienv(etiqueta1), menu_acceder(window)]) # Oculta todos los botones de manejo interno y muestra las labels principales




def funcion_papapapappi(window, boton_prom,boton_iniciarses,boton_papapapi, pruebainicses):


    listadatos=wikisoyunal()

    etiquetapapapi = tk.Label(window, text="PAPA",
                            font=("Adobe Garamond Pro Bold", 20))  # Etiqueta de titulo de promedios
    etiquetapapapi.place(x=80, y=90)
    etiquetapapapi.configure(bg=_from_rgb((177, 178, 176)))

    textopapapa = tk.Label(window, wraplength=500, text=listadatos[0],
                     font=("Adobe Garamond Pro", 12))  # Etiqueta de titulo de promedios
    textopapapa.place(x=70, y=140)
    textopapapa.configure(bg=_from_rgb((177, 178, 176)), width=100, anchor="w")

    titulpapapa = tk.Label(window, wraplength=500, text=listadatos[1][0],
                           font=("Adobe Garamond Pro Bold", 20))  # Etiqueta de titulo de promedios
    titulpapapa.place(x=70, y=270)
    titulpapapa.configure(bg=_from_rgb((177, 178, 176)), width=100, anchor="w")

    calculodelpapa=listadatos[1][1]+"\n" +listadatos[1][2]+"\n"+listadatos[1][3]+"\n"+listadatos[1][4]+"\n"+listadatos[1][5]+"\n"+listadatos[1][6]+"\n"+listadatos[1][7]
    textocalpap = tk.Text(window, wrap=WORD, font=("Adobe Garamond Pro", 12), 	insertborderwidth=7 )  # Etiqueta de titulo de promedios
    textocalpap.insert(tk.END, calculodelpapa)
    textocalpap.configure(bg=_from_rgb((177, 178, 176)), width=100, bd=0)
    textocalpap.place(x=70, y=320)

    boton_prom.configure(command=lambda: [pantalla_principal(window,pruebainicses),ocultar_bl(textocalpap),ocultar_bl(titulpapapa),ocultar_bl(etiquetapapapi), ocultar_bl(textopapapa)])
    boton_iniciarses.configure(command=lambda: [pantalla_principal2(window, boton_prom, boton_papapapi,boton_iniciarses, pruebainicses), ocultar_bl(textocalpap),ocultar_bl(titulpapapa),ocultar_bl(etiquetapapapi), ocultar_bl(textopapapa)])


def pantalla_principal2(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses):

    etiqueta1 = tk.Label(window, text="¡Bienvenido!", font=("Adobe Garamond Pro Bold", 30))  # Etiqueta de bienvenida
    etiqueta1.place(x=495, y=125)
    etiqueta1.configure(bg=_from_rgb((177, 178, 176)))

    boton_acceder = tk.Button(window, text="Acceder",bg=_from_rgb((118, 35, 47)), fg="white", width=8, height=1,
                              font=("Adobe Garamond Pro", 18))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_acceder.place(x=550, y=270)

    boton_acceder.configure(command=lambda: [ocultar_bl(boton_crear_cuenta),
                                             ocultar_bl(boton_acceder),
                                             ocultar_bl(etiqueta1), menu_acceder(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses)])

    boton_crear_cuenta = tk.Button(window,
                                   text="Crear Cuenta",
                                   bg=_from_rgb((118, 35, 47)),
                                   fg="white",
                                   width=10,
                                   height=1,
                                   font=("Adobe Garamond Pro",
                                         18))  # Para la funcion agregar command tras una coma = y la funcion
    boton_crear_cuenta.place(x=536, y=200)
    boton_crear_cuenta.configure(command=lambda: [ocultar_bl(boton_crear_cuenta),
                                                  ocultar_bl(boton_acceder),
                                                  ocultar_bl(etiqueta1), funcion_crear_cuenta(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses)])

    boton_papapapi.configure(command=lambda: [ocultar_bl(boton_crear_cuenta), ocultar_bl(boton_acceder), ocultar_bl(etiqueta1),funcion_papapapappi(window, boton_prom,boton_iniciarses, boton_papapapi, pruebainicses)])
    boton_prom.configure(command=lambda: [pantalla_principal(window,pruebainicses), ocultar_bl(boton_crear_cuenta), ocultar_bl(boton_acceder), ocultar_bl(etiqueta1)])


def menu_acceder(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses):
    etiqueta2 = tk.Label(window, text="Usuario", font=("Adobe Garamond Pro", 16))  # Etiqueta de usuario
    etiqueta2.place(x=450, y=225)
    etiqueta2.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=9)
    entry3 = ttk.Entry(window, width=16)
    entry3.place(x=565, y=227, heigh=26)

    etiquetacontra = tk.Label(window, text="Contraseña", font=("Adobe Garamond Pro", 16))  # Etiqueta de usuario
    etiquetacontra.place(x=450, y=263)
    etiquetacontra.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=9)
    entrycont = ttk.Entry(window, width=16, show="*")
    entrycont.place(x=565, y=265, heigh=26)

    boton_regresaracced = tk.Button(window,
                                    text="Regresar",
                                    bg=_from_rgb((118, 35, 47)),
                                    fg="white",
                                    width=10,
                                    height=1,
                                    font=("Adobe Garamond Pro", 18))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_regresaracced.place(x=400, y=320)
    boton_regresaracced.configure(
        command=lambda: [pantalla_principal2(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses),
                         ocultar_menu_acc(etiqueta2, entry3, etiquetacontra, entrycont, boton_regresaracced), ocultar_bl( boton_acceder)])

    boton_papapapi.configure(command=lambda: [ocultar_bl(etiqueta2), ocultar_bl(entry3), ocultar_bl(etiquetacontra),
                                              ocultar_bl(entrycont), ocultar_bl(boton_regresaracced),
                                              funcion_papapapappi(window, boton_prom, boton_iniciarses,
                                                                  boton_papapapi, pruebainicses), ocultar_bl( boton_acceder)])

    boton_prom.configure(command=lambda: [pantalla_principal(window,pruebainicses), ocultar_bl( boton_acceder),ocultar_bl(etiqueta2), ocultar_bl(entry3), ocultar_bl(etiquetacontra), ocultar_bl(entrycont), ocultar_bl(boton_regresaracced)])

    boton_acceder = tk.Button(window,
                                    text="Acceder",
                                    bg=_from_rgb((118, 35, 47)),
                                    fg="white",
                                    width=10,
                                    height=1,
                                    font=("Adobe Garamond Pro", 18))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_acceder.place(x=570, y=320)
    boton_acceder.configure(
        command=lambda:[acceder(window,entrycont, entry3,boton_prom,boton_papapapi, boton_iniciarses, etiqueta2, etiquetacontra, boton_regresaracced, boton_acceder)])


def ocultar_menu_acc(etiqueta2, entry3, etiquetacontra, entrycont, boton_regresaracced):
    etiqueta2.place_forget()
    entry3.place_forget()
    etiquetacontra.place_forget()
    entrycont.place_forget()
    boton_regresaracced.place_forget()


def funcion_crear_cuenta(window,boton_prom,boton_papapapi, boton_iniciarses, pruebainicses):
    etiquetanombre = tk.Label(window, text="Nombre Completo", font=("Adobe Garamond Pro", 16))
    """Etiqueta de Nombre"""
    etiquetanombre.place(x=375, y=125)
    etiquetanombre.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=18)
    entrynombre = ttk.Entry(window, width=16)
    entrynombre.place(x=600, y=127, heigh=26)

    etiquetadocum = tk.Label(window, text="Numero de documento", font=("Adobe Garamond Pro", 16))
    """Etiqueta de documento"""
    etiquetadocum.place(x=375, y=163)
    etiquetadocum.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=18)
    entrydocumen = ttk.Entry(window, width=16)
    entrydocumen.place(x=600, y=165, heigh=26)

    etiquetausuario = tk.Label(window, text="Usuario", font=("Adobe Garamond Pro", 16))
    """Etiqueta de usuario"""
    etiquetausuario.place(x=375, y=201)
    etiquetausuario.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=18)
    entryusuario = ttk.Entry(window, width=16)
    entryusuario.place(x=600, y=203, heigh=26)

    etiquetacontras = tk.Label(window, text="Contraseña", font=("Adobe Garamond Pro", 16))
    """Etiqueta de contraseña"""
    etiquetacontras.place(x=375, y=239)
    etiquetacontras.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=18)
    entrycont = ttk.Entry(window, width=16, show="*")
    entrycont.place(x=600, y=241, heigh=26)

    etiquetaconfirmcontras = tk.Label(window, text="Confirme Contraseña", font=("Adobe Garamond Pro", 16))
    """Etiqueta de confirmar usuario"""
    etiquetaconfirmcontras.place(x=375, y=277)
    etiquetaconfirmcontras.configure(bg=_from_rgb((177, 178, 176)), anchor="e", width=18)
    entryconfirmcont = ttk.Entry(window, width=16, show="*")
    entryconfirmcont.place(x=600, y=279, heigh=26)

    boton_regresar = tk.Button(window,
                               text="Regresar",
                               bg=_from_rgb((118, 35, 47)),
                               fg="white",
                               width=10,
                               height=1,
                               font=("Adobe Garamond Pro", 18))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_regresar.place(x=380, y=320)
    boton_regresar.configure(command=lambda: [pantalla_principal2(window, boton_prom,boton_papapapi, boton_iniciarses, pruebainicses),
                                              ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                                              entrydocumen, etiquetausuario, entryusuario,
                                                              etiquetacontras, entrycont, etiquetaconfirmcontras,
                                                              entryconfirmcont, boton_regresar, boton_crear)])
    boton_crear = tk.Button(window,
                               text="Crear",
                               bg=_from_rgb((118, 35, 47)),
                               fg="white",
                               width=10,
                               height=1,
                               font=("Adobe Garamond Pro", 18))
    """Para la funcion agregar command tras una coma = y la funcion"""
    boton_crear.place(x=570, y=320)
    boton_crear.configure(command=lambda: [leer_inscripcion(window,entrynombre, entrydocumen, entryusuario, entrycont, entryconfirmcont, boton_prom, boton_papapapi, boton_iniciarses, etiquetanombre, etiquetadocum, etiquetausuario, etiquetacontras, etiquetaconfirmcontras, boton_regresar, boton_crear),
                                           ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                                           entrydocumen, etiquetausuario, entryusuario,
                                                           etiquetacontras, entrycont, etiquetaconfirmcontras,
                                                           entryconfirmcont, boton_regresar, boton_crear)])

    boton_papapapi.configure(
        command=lambda: [ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                                              entrydocumen, etiquetausuario, entryusuario,
                                                              etiquetacontras, entrycont, etiquetaconfirmcontras,
                                                              entryconfirmcont, boton_regresar, boton_crear),
                         funcion_papapapappi(window, boton_prom, boton_iniciarses,
                                             boton_papapapi, pruebainicses)])

    boton_prom.configure(command=lambda: [pantalla_principal(window,pruebainicses), ocultar_bl(etiqueta2), ocultar_bl(entry3),
                                          ocultar_bl(etiquetacontra), ocultar_bl(entrycont),
                                          ocultar_bl(boton_regresaracced)])


def leer_inscripcion(window,entrynombre, entrydocumen, entryusuario, entrycont, entryconfirmcont, boton_prom, boton_papapapi, boton_iniciarses, etiquetanombre, etiquetadocum, etiquetausuario, etiquetacontras, etiquetaconfirmcontras, boton_regresar, boton_crear):

    boton_prom.configure(command=lambda: [pantalla_principal(window,pruebainicses), ocultar_bl(etiqueta2), ocultar_bl(entry3),
                                          ocultar_bl(etiquetacontra), ocultar_bl(entrycont),
                                          ocultar_bl(boton_regresaracced)])

    boton_regresar.configure(command=lambda: [pantalla_principal2(window, boton_prom, boton_papapapi, boton_iniciarses, pruebainicses),
                                              ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                                              entrydocumen, etiquetausuario, entryusuario,
                                                              etiquetacontras, entrycont, etiquetaconfirmcontras,
                                                              entryconfirmcont, boton_regresar, boton_crear)])

    salidaprueba=False

    textoincorre = tk.Label(window,text="Usuario invalido",
                            font=("Adobe Garamond Pro", 12))  # Etiqueta de titulo de promedios
    textoincorre.configure(bg=_from_rgb((177, 178, 176)), width=100, anchor="w")

    textousinv = tk.Label(window, text="Contraseñas no coincidentes",
                          font=("Adobe Garamond Pro", 12))  # Etiqueta de titulo de promedios
    textousinv.configure(bg=_from_rgb((177, 178, 176)), width=100, anchor="w")

    textogood = tk.Label(window, text="Cuenta creada exitosamente",
                            font=("Adobe Garamond Pro", 15))  # Etiqueta de titulo de promedios
    textogood.configure(bg=_from_rgb((177, 178, 176)), width=100, anchor="w")

    usuarios=leer_usuarios()
    nombre = entrynombre.get()
    documento = entrydocumen.get()
    usuario = entryusuario.get()

    contrasenia = entrycont.get()
    confirme_contrasenia = entryconfirmcont.get()
    if contrasenia == confirme_contrasenia:
        for persona in usuarios:
            if persona[2] == usuario:
                textoincorre.place(x=420, y=70)
                ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                entrydocumen, etiquetausuario, entryusuario,
                                etiquetacontras, entrycont, etiquetaconfirmcontras,
                                entryconfirmcont, boton_regresar, boton_crear)
                nombre=" "
                documento =" "
                usuario =" "
                contrasenia =" "
                funcion_crear_cuenta(window,boton_prom,boton_papapapi, boton_iniciarses, pruebainicses)
                salidaprueba=True
        if salidaprueba==True and nombre!=" ":
            f = open('Usuarios.txt', 'a')
            f.write("%"+nombre+"\n")
            f.write(documento + "\n")
            f.write(usuario + "\n")
            f.write(contrasenia + "\n")
            f.close()
            textousinv.place_forget()
            textoincorre.place_forget()
            textogood.place(x=300, y=90)
            pantalla_principal2(window, boton_prom, boton_papapapi, boton_iniciarses, pruebainicses)
            ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                            entrydocumen, etiquetausuario, entryusuario,
                            etiquetacontras, entrycont, etiquetaconfirmcontras,
                            entryconfirmcont, boton_regresar, boton_crear)
    else:
        textousinv.place(x=420, y=90)
        textoincorre.place_forget()
        ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                        entrydocumen, etiquetausuario, entryusuario,
                        etiquetacontras, entrycont, etiquetaconfirmcontras,
                        entryconfirmcont, boton_regresar, boton_crear)
        funcion_crear_cuenta(window, boton_prom, boton_papapapi, boton_iniciarses, pruebainicses)

    boton_papapapi.configure(
        command=lambda: [ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                         entrydocumen, etiquetausuario, entryusuario,
                                         etiquetacontras, entrycont, etiquetaconfirmcontras,
                                         entryconfirmcont, boton_regresar, boton_crear),
                         funcion_papapapappi(window, boton_prom, boton_iniciarses,
                                             boton_papapapi, pruebainicses)])

    boton_prom.configure(command=lambda: [pantalla_pr,pruebainicsesincipal(window), ocultar_bl(etiqueta2), ocultar_bl(entry3),
                                          ocultar_bl(etiquetacontra), ocultar_bl(entrycont),
                                          ocultar_bl(boton_regresaracced)])

    boton_regresar.configure(command=lambda: [pantalla_principal2(window, boton_prom, boton_papapapi, boton_iniciarses, pruebainicses),
                                              ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum,
                                                              entrydocumen, etiquetausuario, entryusuario,
                                                              etiquetacontras, entrycont, etiquetaconfirmcontras,
                                                              entryconfirmcont, boton_regresar, boton_crear)])



def ocultar_crear_c(etiquetanombre, entrynombre, etiquetadocum, entrydocumen, etiquetausuario, entryusuario,
                    etiquetacontras, entrycont, etiquetaconfirmcontras, entryconfirmcont, boton_regresar, boton_crear):
    etiquetanombre.place_forget()
    entrynombre.place_forget()
    etiquetadocum.place_forget()
    entrydocumen.place_forget()
    etiquetausuario.place_forget()
    entryusuario.place_forget()
    etiquetacontras.place_forget()
    entrycont.place_forget()
    etiquetaconfirmcontras.place_forget()
    entryconfirmcont.place_forget()
    boton_regresar.place_forget()
    boton_crear.place_forget()


def main():
    init_window()




main()