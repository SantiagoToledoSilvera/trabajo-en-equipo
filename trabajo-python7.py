# trabajo 7

import random

numero_radm = random.randint(1, 1000)
intentos = 0
max_intentos = 10
adivino = False

while intentos < max_intentos and not adivino:
    intento = int(input("Ingrese un número de el 1 al 1000. "))
    intentos += 1

    if intento < numero_radm:
        print("El número ingresado es MENOR al número por adivinar.")
    elif intento > numero_radm:
        print("El número ingresado es MAYOR al número por adivinar.")
    else: 
        adivino = True    

if adivino == True:
    print(f"Felicidades! Conseguiste el número correcto en {intentos} intentos")
else:
    print(f"Que mal... Se te acabaron los intentos. El número correcto era {numero_radm}")