#Calculadora precio hipoteca
"""Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones: 
Si los ingresos del comprador son de $80.000 o más el pie será del 15% del costo de la casa y el resto se distribuirá en pagos mensuales, a pagar en diez años. 
Si los ingresos del comprador son menos de $80.000 el pie será del 30% del costo de la casa y el resto se distribuirá en pagos mensuales a pagar en 7 años. 
La empresa quiere obtener cuanto debe pagar un comprador por concepto de pie y cuanto por cada pago mensual
"""
print("Calculadora de pie y cuotas.")
ing=float(input("Favor ingrese sus ingresos: "))
while float(ing) <= 0:
    ing=float(input("Sus ingresos no pueden ser negativos: "))
valorcasa=float(input("Favor ingrese el valor de la propiedad: "))
while float(valorcasa) <= 0:
    valorcasa=float(input("La propiedad no puede tener un valor negativo: "))
if float(ing) >= 80000:
    pie1=valorcasa*0.15
    cuot1=(valorcasa-pie1)/120
    print(f"El valor del pie es de {pie1} $ y el valor de las cuotas mensuales es {cuot1} $")
if float(ing) < 80000:
    pie2=valorcasa*0.30
    cuot2=(valorcasa-pie2)/84
    print(f"El valor del pie es de {pie2} $ y el valor de las cuotas mensuales es {cuot2} $")

