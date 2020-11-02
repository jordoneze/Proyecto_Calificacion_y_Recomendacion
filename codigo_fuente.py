def inscripcion(usuarios, materias, tareas):
    nombre = input("Nombre completo: ")
    documento = int(input("Numero de documento: "))
    usuario = input("Usuario: ")
    for persona in usuarios:
        while persona[2] == usuario:
            print("Usuario invalido")
            usuario = input("Usuario: ")
    contrasenia = input("Contraseña: ")
    confirme_contrasenia = input("Confirme su Contraseña: ")
    if contrasenia == confirme_contrasenia:
        usuarios.append([nombre, documento, usuario, contrasenia, materias, tareas])
    else:
        print("Intente de nuevo")
        inscripcion(usuarios, materias, tareas)


def promedio_academico(usuarios, nombre):
    for persona in usuarios:
        if persona[0] == nombre:
            if len(persona[4]) >= 2:
               suma = 0
               sumacreditos = 0
               for materia in persona[4]:
                  if materia[4] == " " or materia[4] == "no" or materia[4] == "No":
                       paso1 = materia[2] * materia[3]
                       suma = suma + paso1
                       sumacreditos = sumacreditos + materia[3]
                  else:
                       None
               promedio_ponderadopa = suma / sumacreditos
               return promedio_ponderadopa


def acceder(usuarios, ret_acceder, nombre):
    nombre = input("Usuario: ")
    contrasenia = input("Contraseña: ")
    for persona in usuarios:
        if nombre == persona[2]:
            if contrasenia == persona[3]:
                ret_acceder = "True"
                maybe_main(usuarios, nombre, ret_acceder)
                return
            else:
                print("Intente de nuevo")
                acceder(usuarios, ret_acceder, nombre)
    print("Usuario invalido")
    acceder(usuarios, ret_acceder, nombre)


def salir():
    print("Hasta pronto")
    exit()


def visualizar_materias(usuarios, nombre):
    for persona in usuarios:
        if persona[2] == nombre:
            print("Materia", '\t', "Codigo", '\t', "Valoracion", '\t', "Creditos", '\t', "Semestre")
            for materias in persona[4]:
                para_imprimir = ""
                if materias[4] == "no" or materias[4] == "No":
                    para_imprimir = str(materias[2]) + '\t'
                elif materias[4] == "Aprueba" or materias[4] == "Desaprueba":
                    para_imprimir = materias[4]
                print(materias[0], '\t'*2, materias[1], '\t'*2, para_imprimir, '\t'*2, materias[3], '\t' * 2, materias[5])


def base(usuarios, nombre):
    nombre_m = input("Nombre de la materia:")
    codigo = input("Codigo de la materia:")
    nota = float(input("Nota:"))
    while nota < 0 or nota > 5:
        print("Fuera de rango")
        nota = float(input("Nota:"))
    creditos = int(input("No. de creditos:"))
    sin_nota = input("Aprueba o desaprueba:")
    semestre_cursado = (int(input("Semestre en el que la curso:")))
    for persona in usuarios:
        if persona[2] == nombre:
            persona[4].append([nombre_m, codigo, nota, creditos, sin_nota, semestre_cursado])
    volver = input("¿Desea agregar mas materias?")
    if volver.lower() == "si" or volver.lower == "yes":
        base(usuarios, nombre)
    elif volver.lower == "no" or volver.lower == "not":
        return persona[4]
    else:
        volver = input("¿Desea agregar mas materias?")
        if volver.lower() == "si" or volver.lower == "yes":
            base(usuarios, nombre)
        elif volver.lower == "no" or volver.lower == "not":
            return persona[4]


def proyectar_nota(total_porcentaje, nota_acumulada, notasaevaluar, porcentajesaevaluar):
    nota_proy = float(input("Nota:"))
    while nota_proy < 0 or nota_proy > 5:
        print("Fuera de rango")
        nota_proy = float(input("Nota:"))
    porcentaje = float(input("Porcentaje:"))
    while porcentaje < 0 or porcentaje > 100:
        print("Fuera de rango")
    notasaevaluar.append(nota_proy)
    porcentajesaevaluar.append(porcentaje)

    agregar_nota = input("¿Desea agregar otra nota?")
    if agregar_nota == "si" or agregar_nota == "Si" or agregar_nota == "yes" or agregar_nota == "Yes":
        proyectar_nota(total_porcentaje, nota_acumulada, notasaevaluar, porcentajesaevaluar)
    for result in range(0, len(notasaevaluar)):
        total_porcentaje = total_porcentaje + porcentajesaevaluar[result]
        nota_acumulada = nota_acumulada + notasaevaluar[result] * (porcentajesaevaluar[result] / 100)
    porcentaje_residuo = (100 - total_porcentaje) / 100
    nota_necesaria = (3.0 - nota_acumulada) / porcentaje_residuo
    return nota_necesaria


def papa(usuarios, nombre):
    for persona in usuarios:
        if persona[0] == nombre:
            if len(persona[4]) < 2:
                None
            else:
                suma = 0
                sumacreditos = 0

                for materia in persona[4]:
                    if materia[4] == " " or materia[4] == "no" or materia[4] == "No":
                        paso1 = materia[2] * materia[3]
                        suma = suma + paso1
                        sumacreditos = sumacreditos + materia[3]
                    else:
                        None
                promedio_ponderadopa = suma / sumacreditos
                return promedio_ponderadopa



def pappi(usuarios, nombre):
    suma = 0
    sumacreditos = 0
    numero_de_semestre = int(input("Semestre que esta cursando:"))
    for persona in usuarios:
        if persona[2] == nombre:
            for para_pappi in persona[4]:
                if para_pappi[4] == " " or para_pappi[4] == "no" or para_pappi[4] == "No":
                    if para_pappi[5] == numero_de_semestre:
                        paso1 = para_pappi[2] * para_pappi[3]
                        suma = suma + paso1
                        sumacreditos = sumacreditos + para_pappi[3]
    if sumacreditos != 0:
        promedio_ponderadopi = suma / sumacreditos
    else:
        promedio_ponderadopi = None
    return promedio_ponderadopi


def agregar_tarea(usuarios, nombre):
    for persona in usuarios:
        if persona[2] == nombre:

            tarea_nueva = input("Nombre de la tarea: ")
            persona[5].append([tarea_nueva, "No"])
            otra = input("¿Agregar otra?: ")
            if otra == "Si" or otra == "si" or otra == "Yes" or otra == "yes":
                agregar_tarea(usuarios, nombre)


def ver_tareas(usuarios, nombre):
    n = 1
    print("No" + ". " + '\t' + "Tarea" + '\t' * 2 + "¿Acabada?")
    for persona in usuarios:
        if persona[2] == nombre:
            for tarea in persona[5]:
                print(str(n) + ". " + '\t' + tarea[0] + '\t' * 2 + tarea[1])
                n = n + 1


def acabar_tareas(usuarios, nombre):
    tarea_acabar = int(input("Tarea por acabar: "))
    for persona in usuarios:
        if persona[2] == nombre:
            tarea_acabada = input("¿Tarea acabada?: ")
            if tarea_acabada == "Si" or tarea_acabada == "si" or tarea_acabada == "yes" or tarea_acabada == "Yes":
                persona[5][tarea_acabar - 1][1] = "Si"
                ocultartarea = True  # ocultar tarea y darla por finalizada, de utilidad al hacer la interfaz grafica
            elif tarea_acabada == "No":
                ocultartarea = False


def pantalla_principal(usuarios, ret_acceder, nombre):
    inicio = input("Acceder o Crear Cuenta: ")
    if inicio.lower() == "crear cuenta":
        materias = []
        tareas = []
        inscripcion(usuarios, materias, tareas)
        pantalla_principal(usuarios, ret_acceder, nombre)
    elif inicio.lower() == "acceder":
        acceder(usuarios, ret_acceder, nombre)
    else:
        pantalla_principal(usuarios, ret_acceder, nombre)


def maybe_main(usuarios, nombre, ret_acceder):
    if ret_acceder == "True":
        print("¿Que desea realizar?")
        print(""" Menu:
    1. Materias
    2. Proyectar notas
    3. Promedio Academico
    4. PAPA(Promedio Academico Ponderado Acumulado)
    5. PAPPI
    6. Tareas
    7. Cerrar sesion
    8. Salir""")
        menu = int(input())
        regresar = True
        while regresar is True:
            if menu == 1:
                print("""   1. Visualizar materias
    2. Agregar materias
    0. Regresar""")
                menu_materias = input()
                if menu_materias == "1":
                    visualizar_materias(usuarios, nombre)
                elif menu_materias == "2":
                    base(usuarios, nombre)
                elif menu_materias == "0":
                    regresar = False

            if menu == 2:
                agregar_nota = input("¿Desea agregar una nota?: ")
                print("La nota para aprobar es 3")
                notasaevaluar = []
                nota_acumulada = 0
                porcentajesaevaluar = []
                total_porcentaje = 0
                if agregar_nota == "si" or agregar_nota == "Si" or agregar_nota == "yes" or agregar_nota == "Yes":
                    nota_necesaria = proyectar_nota(total_porcentaje, nota_acumulada, notasaevaluar, porcentajesaevaluar)
                    print(round(nota_necesaria, 2))
                else:
                    volver = input("¿Regresar?")
                    if volver.lower() == "si" or volver.lower() == "yes":
                        regresar = False

            if menu == 3:
                evaluar_promacad = promedio_academico(usuarios, nombre)
                if evaluar_promacad is None:
                    print("Aun no tiene los datos necesarios para realizar el proceso.")
                else:
                    print("Su promedio academico es:" + str(round(evaluar_promacad, 1)))

            if menu == 4:
                evaluar_papa = papa(usuarios, nombre)
                if evaluar_papa is None:
                    print("Aun no tiene los datos necesarios para realizar el proceso.")
                else:
                    print("Su PAPA es:" + str(round(evaluar_papa, 1)))
                    if evaluar_papa>=4.5:
                        print("Estudiante Excepcional. ¡Excelente!.")
                    elif evaluar_papa>=4.3 and evaluar_papa<=4.4:
                        print("Estudiante destacado, muy bien.")
                    elif evaluar_papa>=4 and evaluar_papa<=4.2:
                        print("Buen estudiante, por encima del promedio.")
                    elif evaluar_papa>=4 and evaluar_papa<=4.2:
                        print("¡Continua así!")
                    elif evaluar_papa >= 3.4 and evaluar_papa <= 3.6:
                        print("¡Tienes que esforzarte un poco mas!")
                    elif evaluar_papa >= 3 and evaluar_papa <= 3.3:
                        print("¡Tienes que esforzarte mas!")

            if menu == 5:
                promedio_pondeppi = pappi(usuarios, nombre)
                print("Su PAPPI es:" + str(round(promedio_pondeppi, 2)))

            if menu == 6:
                print("""   1. Visualizar Tareas
    2. Agregar Tareas
    3. Finalizar Tareas
    0. Regresar""")
                menu_tareas = input()
                if menu_tareas == "1":
                    ver_tareas(usuarios, nombre)
                elif menu_tareas == "2":
                    agregar_tarea(usuarios, nombre)
                elif menu_tareas == "3":
                    acabar_tareas(usuarios, nombre)
                elif menu_tareas == "0":
                    regresar = False
                    # Rellenar Funcion

            if menu == 7:
                main1(usuarios, nombre, ret_acceder)
            if menu == 8:
                salir()
            else:
                print("Fuera de rango")
                maybe_main(usuarios, nombre, ret_acceder)

        maybe_main(usuarios, nombre, ret_acceder)


def main1(usuarios, nombre, ret_acceder):
    print("Bienvenido")

    pantalla_principal(usuarios, ret_acceder, nombre)
    maybe_main(usuarios, nombre, ret_acceder)


def main():
    usuarios = []
    nombre = ""
    ret_acceder = "False"
    main1(usuarios, nombre, ret_acceder)


main()
