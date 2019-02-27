# Jesús Eduardo Ramírez Cota - 165732
# Programa que calcula la comision de un vendedor de acuerdo a sus ventas.
montoVentas = 0.0
comision = 0.0
# Se ingresa el monto de ventas del vendedor.
montoVentas = float(input("Indique el monto del vendedor: "))


# Se establece el porcentaje de comisión de acuerdo al monto de venta
if montoVentas >= 1000.00 and montoVentas <=4999.99 : comision = 0.025
elif montoVentas >= 5000.00 and montoVentas <=9999.99: comision = 0.05
elif montoVentas >= 10000.00 and montoVentas <=49999.99: comision = 0.075
elif montoVentas >= 50000.00: comision = 0.1

# Se calcula el monto de comisión de acuerdo al monto de venta y al porcentaje de comisión.
comision = montoVentas*comision
print("Comisión del vendedor: " +str(round(comision,2)))