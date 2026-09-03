###Mi Primer Objeto###

class Person:
    def __init__(self,name ,age): 
        self.name = name
        self.age = age

    def Dormir(self):
        print(self.name, "está durmiendo")

#name = input("Ingrese su nombre: ")
#age = int(input("Ingrese su edad: "))

person = Person("Maurcio", 32)
person2 = Person("Juan", 30)
print(person.name, person.age)
print(person2.name, person2.age)
person.Dormir()

#Crear un objeto laptop con 2 atributos y que el comportamiento sea encender.

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def encender(self):
        print(f"The {self.brand} laptop {self.model} is on.")

laptop = Laptop("Dell", "Latitude 5300")
print(laptop.brand, laptop.model)
laptop.encender()

#crear un objeto cuenta

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"El saldo actual de {self.titular} es: {self.saldo}")

cuenta = Cuenta("Mauricio", 2000)
while True:
    print("1. mostrar Cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    op = int(input("Ingrese una opción: "))
    if op == 1:
        cuenta.mostrar_saldo()
    elif op == 2:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif op == 3:
        retirar = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(retirar)
    elif op == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}")

producto = Producto("Arroz", 1500)
print(producto.nombre, producto.precio)
producto.mostrar_info()

#Los Atributos son las caracteristicas del objeto y los metodos son las acciones que puede realizar el objeto.

