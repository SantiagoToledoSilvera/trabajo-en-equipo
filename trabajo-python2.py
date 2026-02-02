n = int(input("Ingrese un numero maximo para encontrar los primos: "))


for i in range(2, n+1,):
    if i == 2 * i and i  == 3 * i:
        continue
    print(f"{i}", end = " ")

          

