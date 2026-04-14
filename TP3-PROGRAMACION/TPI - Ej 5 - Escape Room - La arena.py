vida_gladiador = 100
vida_enemigo = 100

nombre_gladiador = ""

pociones_vida = 3

en_juego = True
turno_gladiador = True

danio_ataque_pesado = 15
danio_base_enemigo = 12
danio_base_gladiador = 12

#configuración del personaje
print("--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Nombre del Gladiador: ")
while (not nombre_gladiador.isalpha()):
    nombre_gladiador = input("Error: sólo se permiten letras. ")

print("=== INICIO DEL COMBATE ===")
while(en_juego):

    print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones : {pociones_vida}")

    print("Elige acción: ")
    print("1) Ataque Pesado")
    print("2) Ráfaga Veloz")
    print("3) Curar ")
    opcion = input(" > Opción: ")
    while (not opcion.isdigit() or int(opcion) not in range(1,4)):
        opcion = input("Error: Ingrese un número válido. ")

    opcion = int(opcion)
    if(opcion == 1):
        #Ataque Pesado
        if(vida_enemigo < 20):
            danio_base_gladiador *= 1.5
        vida_enemigo -= danio_base_gladiador

        print(f">> ¡Atacaste al enemigo por {danio_base_gladiador} puntos de daño!")
    elif(opcion == 2):
        #Ráfaga Veloz    
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range (0, 3):
            vida_enemigo -= 5
            print(">Golpe conectado por 5 de daño.")
    else:
        #Opción 3 - Curar
        if(pociones_vida > 0):
            vida_gladiador += 30
            if(vida_gladiador > 100):
                vida_gladiador = 100
            pociones_vida -= 1
        else:
            print("¡No quedan pociones!")

    #Turno del enemigo
    vida_gladiador -= danio_base_enemigo
    print("¡El enemigo contraataca por 12 puntos de daño!")

    en_juego = vida_enemigo > 0 and vida_gladiador > 0
    if(en_juego):
        print(" === NUEVO TURNO === ")


#se terminó el juego
if(vida_gladiador > 0):
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla. ")
else:
    print("DERROTA. Has caído en combate. ")
