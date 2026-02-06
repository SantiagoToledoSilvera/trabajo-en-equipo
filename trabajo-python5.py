# Trabajo 5

car = input("Ingresa los 50 caracteres que quieres filtrar. ").strip()

caracteres = 0


for num in car:
    if num == "a":
        caracteres += 1

print(f"La cantidad de 'a' que hay en los valores ingresados es de {caracteres}")
