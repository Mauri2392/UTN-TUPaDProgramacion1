
total_sin_dto = 0
total_con_dto = 0
ahorro = 0
promedio_por_producto = 0

nombre = input("Ingrese nombre del cliente: ")
while(not nombre.isalpha()):
    nombre = input("Error: Ingrese un nombre con letras. ")

print(f"Cliente: {nombre}")

cant_prod = input("Ingrese la cantidad de productos a comprar: ")
while(not cant_prod.isdigit() or int(cant_prod) == 0):
    cant_prod = input("Ingrese un numero entero: ")
cant_prod = int(cant_prod)
print(f"Cantidad de productos: {cant_prod}")

for x in range(int(cant_prod)):
    precio = input(f"Ingrese el precio del producto {x+1}: ")
    while(not precio.isdigit()):
        precio = input(f"Ingrese un numero entero: ")

    precio = int(precio)
    total_sin_dto += precio
    descuento = input("¿El producto tiene descuento (S/N)?: ")
    si = ['s', 'S']
    no = ['n', 'N']
    opciones = si + no
    
    while(not descuento in(opciones)):
        descuento = input("Ingrese S o N: ")
        
    print(f"Producto {x+1} - Precio: {precio} Descuento (S/N): {descuento}" )

    if(descuento in si):
        ahorro += precio*0.1
        precio_final = precio - precio*0.1
    else:
        precio_final = precio

    total_con_dto += precio_final

    
promedio_por_producto = total_con_dto/cant_prod

print(f"Total sin descuentos: ${total_sin_dto}")
print(f"Total con descuentos: ${total_con_dto:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")
