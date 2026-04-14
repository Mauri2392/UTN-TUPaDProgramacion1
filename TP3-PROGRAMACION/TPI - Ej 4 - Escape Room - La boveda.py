energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
forzar_exec = 0
en_juego = True
estado_juego_final = ""

msj_nombre_ag = "Nombre del agente (no se permiten numeros): "
msj_menu = "1) Forzar cerradura     2) Hackear panel    3) Descansar"
msj_numero = "Ingrese un número del 1 al 3: "

nombre_agente = input(msj_nombre_ag)
while (not nombre_agente.isalpha()):
    nombre_agente = input(msj_nombre_ag)

while(en_juego):
    print(f"Energía: {energia} - Tiempo: {tiempo} - Cerraduras abiertas: {cerraduras_abiertas} - Alarma: {alarma}")
    print(msj_menu)
    opcion = input(" > Opción: ")

    while (not opcion.isdigit() or int(opcion) not in range(1,4)):
        opcion = input(" > Opción del 1 al 3: ")
    
    opcion = int(opcion)
    if(opcion == 1):
        #Forzar cerradura
        energia = energia - 20
        tiempo = tiempo - 2
        forzar_exec = forzar_exec + 1
        if(forzar_exec >= 3):
            #regla antispam
            alarma = True
        if(energia < 40):
            #riesgo de alarma
            print("RIESGO DE ALARMA")
            numero = input(msj_numero)
            while(not numero.isdigit() or not int(numero) in range(1,4)):
                numero = input(msj_numero)
            numero = int(numero)
            if(numero == 3):
                alarma = True
        if(not alarma):
            cerraduras_abiertas +=1
    elif(opcion == 2):
        #Hackear panel
        energia -= 10
        tiempo -= 3
        forzar_exec = 0
        for i in range(1,5):
            codigo_parcial = codigo_parcial+'A'
            print(f"Paso {i}, código parcial {codigo_parcial}")
        if(len(codigo_parcial) >= 8 and cerraduras_abiertas < 3):
            print(len(codigo_parcial))
            cerraduras_abiertas += 1
    else:
        #(opción 3) Descansar
        if(energia <= 75):
            energia += 15
        else:
            energia = 100
        if(alarma):
            energia -= 10
        tiempo -= 1    
        forzar_exec = 0

    if(cerraduras_abiertas == 3):
        estado_juego_final = "VICTORIA"
        en_juego = False
    elif(energia <= 0 or tiempo <= 0 or alarma and tiempo <= 3):
        estado_juego_final = "DERROTA"
        en_juego = False

print(f"¡FINAL DEL JUEGO! Resultado: {estado_juego_final} ")
print("Estado final: ")
print(f">> Energía: {energia}")
print(f">> Tiempo: {tiempo}")
print(f">> Alarma: {alarma} ")
print(f">> Cerraduras abiertas: {cerraduras_abiertas} ")
