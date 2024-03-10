#Nombre y explique brevemente los pilares de POO
# Abstracción: Capacidad de llevar una entidad a su mas sencilla interpretación
# Encapsulamiento: Poder organizar los modulos de manera independiente.
# Herencia: Capacidad de los objetos de heredar atributos y funciones de otros.
# Ocultamiento: Poder mantener los datos ocultos si no se utilizan los metodos del objeto para su obtención
#Explique y ejemplifique el concepto de clase
# La clase es por decirlo de cierta manera, un molde que los lineamientos (atributos y metodos) para crear una instancia u objeto.
#Explique y ejemplifique el concepto de objeto
# El objeto es una instancia de una clase, es la entidad que fue creada de acuerdo al molde (clase) y que tendra los atributos del objeto.

class Persona():
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
    def get_edad(self):
        return self.__edad
    def get_nombre(self):
        return self.__nombre
    def get_sexo(self):
        return self.__sexo
    def set_edad(self,x):
        self.__edad=x
    def set_nombre(self,x):
        self.__nombre=x
    def set_sexo(self,x):
        self.__sexo=x
class Profesion(Persona):
    def __init__(self, nombre, edad, sexo, sueldo, profesion):
        super().__init__(nombre,edad,sexo)
        self.__sueldo=sueldo
        self.__profesion=profesion
    def get_sueldo(self):
        return self.__sueldo
    def get_profesion(self):
        return self.__profesion
    def set_sueldo(self,x):
        self.__sueldo = x
    def set_profesion(self,x):
        self.__profesion = x
op = int (0)
suel4=0;suel2=0;suel6=0
abo=int(0);inge=int(0);otro=int(0)
while int(op) != int(1):
    print("\tBienvenido a la encuesta.")
    nombre=input("Favor ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    while int(edad) < int (1):
        edad=int(input("Su edad no puede ser un numero inferior a 0: "))
    sexo=input("Por favor indique su genero, Masculino o Femenino: ")
    prof=input("Por favor indique su profesion, Ingeniero, Abogado u Otro: ")
    while str(prof).lower() != str("Abogado").lower() and str(prof).lower() != str("Ingeniero").lower() and str(prof).lower() != str("Otro").lower():
        prof=input ("Solo puede introducir las opciones mencionadas, Abogado, Ingeniero u Otro: ")
    suel=input("Introduzca su sueldo: ")
    while float(suel) < 0:
        suel=input("Su sueldo no puede ser un numero negativo: ")
    p1=Profesion(nombre,edad,sexo,suel,prof)
    x=Profesion.get_profesion(p1)
    if x.lower() == str("Abogado").lower():
        abo=int(abo)+int(1)
        suel1=float(Profesion.get_sueldo(p1))
        suel2=suel2+suel1         
    elif x.lower() == str("Ingeniero").lower():
        inge=int(inge)+int(1)
        suel3=float(Profesion.get_sueldo(p1))
        suel4=suel4+suel3
    elif x.lower() == str("Otro").lower():
        otro=int(otro)+int(1)
        suel5=float(Profesion.get_sueldo(p1))
        suel6=suel6+suel5
    op=int(input("Quiere añadir otra persona?: 1 para No, 0 para Si: "))
    while int(op) < 0 and int(op) > 99999999999999:
        op=int(input("La opcion debe ser un numero mayor a 0"))
promabo=suel2/abo
prominge=suel4/inge
promotro=suel6/otro
total=abo+inge+otro
porcentabo=(abo/total)*100
porcentinge=(inge/total)*100
porcentotro=(otro/total)*100
promediosuelge=(suel2+suel4+suel6)/total
print("\tResultados de la encuesta: ")
print("La cantidad total de encuestados es: ",total)
print(f"El porcentaje de cada profesión es: \t Abogados {porcentabo}% \t Ingenierios {porcentinge}% \t Otros {porcentotro}%")
print(f"El promedio de sueldo por profesión es: \t Abogados {promabo} $ \t Ingenieros {prominge} $ \t Otros {promotro} $")
print(f"El promedio de sueldo general es: {promediosuelge}")

