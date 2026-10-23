#Ejercicio 3
 
def valor_absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero
 
 
def es_aceptable(medicion, objetivo, tolerancia):
    error = valor_absoluto(medicion - objetivo)
    if error <= tolerancia:
        return True
    else:
        return False
 
 
objetivo = float(input("Objetivo: "))
tolerancia = float(input("Tolerancia: "))
medicion1 = float(input("Medición 1: "))
medicion2 = float(input("Medición 2: "))
 
print("Medición 1 aceptable:", es_aceptable(medicion1, objetivo, tolerancia))
print("Medición 2 aceptable:", es_aceptable(medicion2, objetivo, tolerancia))