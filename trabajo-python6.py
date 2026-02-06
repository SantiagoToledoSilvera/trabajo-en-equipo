# trabajo 6

contador = 0
suma_sueldos = 0
mayor_sueldo = 0
orden_mayor = None

while True:
    orden = int(input("Ingrese número de orden del empleado: "))
    sueldo = float(input("Ingrese sueldo (0 o negativo para terminar): "))

    if sueldo <= 0:
        break

    contador += 1
    suma_sueldos += sueldo

    if sueldo > mayor_sueldo:
        mayor_sueldo = sueldo
        orden_mayor = orden

if contador > 0:
    promedio = suma_sueldos / contador
    print("\nRESULTADOS")
    print(f"Empleado con mayor sueldo: {orden_mayor}")
    print(f"Mayor sueldo: {mayor_sueldo}")
    print(f"Cantidad de sueldos ingresados: {contador}")
    print(f"Promedio de sueldos: {promedio}")
else:
    print("No se ingresaron sueldos válidos.")
