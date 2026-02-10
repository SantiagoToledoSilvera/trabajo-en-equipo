# trabajo 8

import random

# Pedir el número de puntos
N = int(input("Ingrese la cantidad de puntos a generar: "))

# Contadores
puntos_dentro = 0

# Generar los puntos
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Verificar si el punto está dentro del círculo
    if x**2 + y**2 <= 1:
        puntos_dentro += 1

# Calcular aproximación de pi
pi_aproximado = 4 * puntos_dentro / N

# Mostrar resultados
print("Número total de puntos:", N)
print("Puntos dentro del círculo:", puntos_dentro)
print("Valor aproximado de pi:", pi_aproximado)