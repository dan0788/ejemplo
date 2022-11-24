descuento = 0.0
sueldo = float(input("Ingrese el sueldo del trabajador: "))
if sueldo <= 1000:
    descuento = sueldo*0.1
elif sueldo > 1000 and sueldo <= 2000:
    descuento = sueldo*0.15
elif sueldo > 2000:
    descuento = sueldo*0.18
neto = sueldo - descuento
print("El descuento del trabajador es: ", descuento)
print("El sueldo neto del trabajador es: ", neto)