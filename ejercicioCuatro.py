#Ejercico 4
 
def pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = 40 * tarifa + (horas - 40) * tarifa * 1.5
    return pago
 
 
horas1 = float(input("Horas persona 1: "))
tarifa1 = float(input("Tarifa persona 1: "))
horas2 = float(input("Horas persona 2: "))
tarifa2 = float(input("Tarifa persona 2: "))
 
pago1 = pago_semanal(horas1, tarifa1)
pago2 = pago_semanal(horas2, tarifa2)
total = pago1 + pago2
 
print("Pago persona 1:", pago1, "pesos")
print("Pago persona 2:", pago2, "pesos")
print("Total:", total, "pesos")