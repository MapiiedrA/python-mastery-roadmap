### COA2 ###

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"El Vehiculo {self.marca} esta encendido.")

class Automovil(Vehiculo):
    def abrir_maletero(self):
        print("Maletero Abierto")

carro1 = Automovil("Toyota")
carro1.encender()
carro1.abrir_maletero()

class Persona:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def mostrar_datos(self):
        return "Nombre" + self.name + "\nEdad" + str(self.age)

class Estudiante(Persona):
    def __init__(self, name, age, carrera):
        super().__init__(name, age)
        self.carrera = carrera
    def estudiar(self):
        return "Estudia: " + self.carrera

estu1 = Estudiante("Maroto", 45, "Info")
print(estu1.mostrar_datos())
print(estu1.estudiar)


class Dispositivo:
    def __init__(self, brand, model, batery):
        self.brand = brand
        self.model = model
        self.batery = batery

    def charge(self):
        self.batery = 90

    def mostrar_info(self):
        print(self.brand, self.model, self.batery)

class Celular(Dispositivo):
    def __init__(self, brand, model, batery, storage):
        super().__init__(brand, model, batery)
        self.storage = storage

    def tomar_foto(self):
        print("Foto Tomada")

    def mostrar_celular(self):
        self.mostrar_info()
        print(f"Almacenamiento: {self.storage}GB")


telefono = Celular("Oneplus", "7", 90, "100")
telefono.tomar_foto()
telefono.mostrar_celular()

class Animal:
    def hacer_sonido(self):
        print("Sonido desconocido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Hace Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Hace Miau")

class Pato(Animal):
    def hacer_sonido(self):
        print("Hace Quack")

animales = [Perro(), Gato(), Pato()]
for i in animales:
    i.hacer_sonido()

class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        print("Enviar Notificacion")

class Email(Notificacion):
    def enviar(self):
        print(f"Enviar Email: '{self.mensaje}'")


class SMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS: '{self.mensaje}'")


class WhatsApp(Notificacion):
    def enviar(self):
        print(f"Enviar WhatsApp: '{self.mensaje}'")

if __name__ == "__main__":
    notif1 = Email("Esto es Spam")
    notif2 = SMS("Tu pin es 4821")
    notif3 = WhatsApp("Ya voy llegando")

    notificaciones = [notif1, notif2, notif3]
    print("NOTIFICACIONES")
    for notificacion in notificaciones:
        notificacion.enviar()