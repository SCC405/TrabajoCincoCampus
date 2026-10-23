# Ejercicio 1
 
def area_triangulo(base, altura):
    area = base * altura / 2
    return area
 
 
base1 = float(input("Base 1: "))
altura1 = float(input("Altura 1: "))
base2 = float(input("Base 2: "))
altura2 = float(input("Altura 2: "))
 
area1 = area_triangulo(base1, altura1)
area2 = area_triangulo(base2, altura2)
suma = area1 + area2
 
print("Área 1:", area1, "cm²")
print("Área 2:", area2, "cm²")
print("Suma:", suma, "cm²")