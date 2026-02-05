n = int(input("Ingrese un numero maximo para encontrar los primos: "))

primo = [True] * (n + 1)

primo[0] = False
primo[1] = False

for num in range (2, int(n ** 0.5) + 1):
    if primo[num]:
        for no_prim_num in range(num * num, n + 1, num):
            primo[no_prim_num] = False

lista_primos = [] 
for num in range(2, n + 1):
    if primo[num]:
        lista_primos.append(num)

print("La cantidad de números es", len(lista_primos), "y los números son: ", lista_primos)

          

