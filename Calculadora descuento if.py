#Calculadora de descuento entradas
"""Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro deja de percibir por cada una de las categorías. 
Tomar en cuenta que los niños menores de 5 años no pueden entrar al teatro y que existe un precio único en los asientos. 
Los descuentos se hacen tomando en cuenta el siguiente cuadro:
Edad Descuento
Categoría 1 	  5 - 14 		35 %
Categoría 2 	15 - 19 		25 %
Categoría 3 	20 - 45 		10 %
Categoría 4 	46 - 65 		25 %
Categoría 5 	66 en adelante 	35 %
"""
cat1=0;cat2=0;cat3=0;cat4=0;cat5=0
valentrada=float(input("Ingrese el valor de la entrada: "))
while valentrada <= 0:
    valentrada=float(input("El valor no puede ser negativo: "))
op=int(0)
while op < 1:
    edad=int(input("Indique su edad: "))
    while edad < 5:
        edad=int(input("Solo se admiten personas mayores de 5 años: "))
    if int(edad) >= 5 and int(edad) <= 14:
        cat1=cat1+1
    if int(edad) >= 15 and int (edad) <= 19:
        cat2=cat2+1
    if int(edad) >= 20 and int (edad) <= 45:
        cat3=cat3+1
    if int(edad) >= 46 and int(edad) <= 65:
        cat4=cat4+1
    if int(edad) >= 66:
        cat5=cat5+1
    op=int(input("Quiere comprar otra entrada? 0 para si, 1 para no: "))
val1=(valentrada*cat1)*0.35
val2=(valentrada*cat2)*0.25
val3=(valentrada*cat3)*0.10
val4=(valentrada*cat4)*0.25
val5=(valentrada*cat5)*0.35

print(f"El descuento en entradas de categoria 1 es {val1} $")
print(f"El descuento en entradas de categoria 2 es {val2} $")
print(f"El descuento en entradas de categoria 3 es {val3} $")
print(f"El descuento en entradas de categoria 4 es {val4} $")
print(f"El descuento en entradas de categoria 5 es {val5} $")