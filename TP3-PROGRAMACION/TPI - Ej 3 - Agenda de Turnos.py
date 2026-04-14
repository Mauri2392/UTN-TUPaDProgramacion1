cupos_lun = 4
cupos_mar = 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre_op = input("Nombre del operador: ")
while (not nombre_op.isalpha()):
    nombre_op = input("Introduzca un nombre con letras: ")

en_sesion = True

while(en_sesion):
    print("\n1) Reservar turno    2) Cancelar turno    3) Ver agenda del día    4) Ver resumen general    5) Cerrar sistema. ")
    opcion = input(" > Opción: ")
    while (not opcion.isdigit() or int(opcion) not in range(1,6)):
        opcion = input(" > Opción: ")

    opcion = int(opcion)
    msj_dia = "Elegir día ingresando el numero: Lunes (1) ó Martes (2): "
    msj_no_disponible = "No hay turnos disponibles este día. "
    msj_nombre_paciente = "Nombre del paciente: " 

    if(opcion == 1):
        dia = input(msj_dia)
        while(not dia.isdigit() or int(dia) not in range(1,3)):
            dia = input(msj_dia)
        paciente = input(msj_nombre_paciente)
        while(not paciente.isalpha()):
            paciente = input(msj_nombre_paciente)
        encontre = False
        i = 1
        dia = int(dia)
        turno_creado = False

        if(dia == 1):
            #lunes
            encontre = paciente in (lunes1, lunes2, lunes3, lunes4)
            if(encontre):
                print("El paciente ya tiene un turno reservado ese día. ")
            else:
                if(lunes1 == ""):
                    lunes1 = paciente
                    turno_creado = True
                elif(lunes2 == ""):
                    lunes2 = paciente
                    turno_creado = True
                elif(lunes3 == ""):
                    lunes3 = paciente
                    turno_creado = True
                elif(lunes4 == ""):
                    lunes4 = paciente
                    turno_creado = True
                else:
                    #no hay lugares
                    print(msj_no_disponible)
        else:
            #martes                
            encontre = paciente in (martes1, martes2, martes3)
            if(encontre):
                print("El paciente ya tiene un turno reservado ese día. ")
            else:
                if(martes1 == ""):
                    martes1 = paciente
                    turno_creado = True
                elif(martes2 == ""):
                    martes2 = paciente
                    turno_creado = True
                elif(martes3 == ""):
                    martes3 = paciente
                    turno_creado = True
                else:
                    #no hay lugares
                    print(msj_no_disponible)
        if(turno_creado):
            print("Turno reservado con éxito. ")
    elif(opcion == 2):
        #cancelar
        dia = input(msj_dia)
        while(not dia.isdigit() or int(dia) not in range(1,3)):
            dia = input(msj_dia)
        paciente = input(msj_nombre_paciente)
        while(not paciente.isalpha()):
            paciente = input(msj_nombre_paciente)

        dia = int(dia)
        existe = False
        if(dia == 1):
            #lunes
            if(lunes1 == paciente):
                lunes1 = ""
                existe = True
            elif(lunes2 == paciente):
                lunes2 = ""
                existe = True
            elif(lunes3 == paciente):
                lunes3 = ""
                existe = True
            elif(lunes4 == paciente):
                lunes4 = ""
                existe = True
        else:
            #martes
            if(martes1 == paciente):
                martes1 = ""
                existe = True
            elif(martes2 == paciente):
                martes2 = ""
                existe = True
            elif(martes3 == paciente):
                martes3 = ""
                existe = True
        if(existe):
            print("Turno cancelado.")
        else:
            print("No existe turno reservado para ese paciente en ese día.")
    elif(opcion == 3):
        #Ver agenda del día
        dia = input(msj_dia)
        while(not dia.isdigit() or int(dia) not in range(1,3)):
            dia = input(msj_dia)
        
        dia = int(dia)
        if(dia == 1):
            #Lunes
            print("-- Lunes --")
            if(lunes1 == ""):
                print("T1: Libre. ")
            else:
                print(f"T1: {lunes1}")
            if(lunes2 == ""):
                print("T2: Libre. ")
            else:
                print(f"T2: {lunes2}")
            if(lunes3 == ""):
                print("T3: Libre. ")
            else:
                print(f"T3: {lunes3}")
            if(lunes4 == ""):
                print("T4: Libre. ")
            else:
                print(f"T4: {lunes4}")
        else:
            #martes
            print("-- Martes --")

            if(martes1 == ""):
                print("T1: Libre. ")
            else:
                print(f"T1: {martes1}")
            if(martes2 == ""):
                print("T2: Libre. ")
            else:
                print(f"T2: {martes2}")
            if(martes3 == ""):
                print("T3: Libre. ")
            else:
                print(f"T3: {martes3}")
    elif(opcion == 4):
        #ver resumen general
        turnos_lunes = 0
        turnos_martes = 0
        
        print("Agenda general: ")

        if(lunes1 != ""):
            turnos_lunes += 1
        if(lunes2 != ""):
            turnos_lunes += 1
        if(lunes3 != ""):
            turnos_lunes += 1
        if(lunes4 != ""):
            turnos_lunes += 1
            
        if(martes1 != ""):
            turnos_martes += 1
        if(martes2 != ""):
            turnos_martes += 1
        if(martes3 != ""):
            turnos_martes += 1
        
        print(f"Lunes: turnos reservados {turnos_lunes}")
        print(f"Martes: turnos reservados {turnos_martes}")
        msj_turnos = "Empate."
        if(turnos_lunes > turnos_martes):
            msj_turnos = "Lunes."
        elif(turnos_martes > turnos_lunes):
            msj_turnos = "Martes."
        print(f"Día con más turnos: {msj_turnos}")
    else:
        #salir
        print("Cerrando sesión...")
        en_sesion = False 