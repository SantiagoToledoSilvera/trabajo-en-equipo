# Trabajo 4

n = int(input("Ingrese un numero entero de varios digitos: "))

invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10

print(f"El número ingresado invertido seria: {invertido}")