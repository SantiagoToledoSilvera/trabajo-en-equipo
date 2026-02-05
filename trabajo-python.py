# Trabajo ejercicios en pareja

print("""
_____________Calculadora de intereses._____________
Ingrese los valores para calcular los intereses  
de un capital por la cantidad de años estimada.
____________________________________________________
""")

def valores():
    c = int(input("¿Cantidad del capital? "))
    i = int(input("¿Porcentaje de intereses? "))
    m = int(input("¿Tiempo estimado de el prestamo? "))
    return (c * i) / 100 * m
    
print(f"{valores():.0f}")