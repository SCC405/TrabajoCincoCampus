#Ejercicio 2
 
def precio_por_gramo(precio, gramos):
    precio_gramo = precio / gramos
    return precio_gramo
 
 
precio1 = float(input("Precio paquete 1: "))
gramos1 = float(input("Gramos paquete 1: "))
precio2 = float(input("Precio paquete 2: "))
gramos2 = float(input("Gramos paquete 2: "))
 
p1 = precio_por_gramo(precio1, gramos1)
p2 = precio_por_gramo(precio2, gramos2)
 
print("Precio por gramo paquete 1:", p1, "pesos")
print("Precio por gramo paquete 2:", p2, "pesos")
 
if p1 < p2:
    print("Conviene paquete 1")
elif p2 < p1:
    print("Conviene paquete 2")
else:
    print("Son iguales")