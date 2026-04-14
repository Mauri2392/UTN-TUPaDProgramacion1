usuario = "alumno"
password = "python123"
max_intentos = 3
acceso_valido = False

print("Ingreso a cuenta...")

i = 1
print(f"\nIntento {i}/{max_intentos} - Usuario: {usuario}")
pass_ingresado = input("Clave: ")
acceso_valido = pass_ingresado == password
i += 1

while( i <= max_intentos and (not acceso_valido)):
    print("Error: credenciales inválidas. ")
    print(f"\nIntento {i}/{max_intentos} - Usuario: {usuario}")
    pass_ingresado = input("Clave: ")
    acceso_valido = pass_ingresado == password
    i += 1

if(acceso_valido):
    print("\nAcceso concedido.")
    print(" 1) Estado    2) Cambiar clave    3) Mensaje     4) Salir ")
    en_sesion = True

    while(en_sesion):
        opcion = input(" > Elija una Opción: ")
        if(not opcion.isdigit()):
            print("Error: ingrese un número válido. ")
            continue
        opcion = int(opcion)
        if(opcion not in range(1,5)):
            print("Error: opción fuera de rango. ")
            continue
    
        if(opcion == 1):
            print("Estado: Inscripto")
        elif(opcion == 2):
            nueva_clave = input("Nueva clave: ")
            while(len(nueva_clave) < 6):
                nueva_clave = input("Error: mínimo 6 caracteres. Nueva clave: ")
            
            confirmacion = input("Repetir nueva clave: ")
            while(nueva_clave != confirmacion):
                confirmacion = input("Las contraseñas no coinciden. Intentelo nuevamente: ")
            password = nueva_clave
            print("La clave ha sido actualizada. ")
        elif(opcion == 3):
            print("  ~ Yo se que vas a poder aprobar la materia. ~ ")
        else:
            print("Cerrando sesión... ")
            en_sesion = False                
else:
    print("\nCuenta bloqueada. ")


