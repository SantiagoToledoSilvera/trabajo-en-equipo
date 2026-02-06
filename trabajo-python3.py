# Trabajo 3

x = float(input("Ingresa el valor de x. "))
n = int(input("Ingrese la cantidad de términos: "))

resultado = 0
factorial = 1

for cont in range(n + 1):
    if cont > 0:
        factorial *= cont
    resultado += (x ** cont) / factorial

print(f"El valor aproximado de e^{x} es: {resultado}")
