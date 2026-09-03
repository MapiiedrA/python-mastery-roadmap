### Classes ###              ####Sirve para identificar nuestro condigo dentro de un ambito en especifico ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:   #Como buena practica para el lenguaje es mejor ponerla primera letra en mayus y no en SnakeChase.
    def __init__(self, name, surname):      #__init__ es un constructor de clase
        self.name = name
        self.surname = surname

my_person = Person("Mauricio", "Piedra")
print(my_person.name)

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Mauricio", "Piedra")
print(my_person.full_name)
my_person.walk()

class Person:
    def __init__(self, name, surname, alias = "Sin Alias"):
        self.full_name = f"{name} {surname} ({alias})" #Los Parentesis en Alias indican que en la cadena de texto quiero quede entre parentesis , pero esa variable puede se entre cualquier otra cosa que yo quiera.

    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Mauricio", "Piedra")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Mauricio", "Piedra", "MapiiedrA")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (el loco de los perros)"
print(my_other_person.full_name)

### Curiosidad de Classes Privadas ###

class Person:  
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}" #Propiedad Publica , Se puede acceder a ella y modificarla.   
        self.__name = name #Propiedad Privada, se puede leer pero no modificarla(name)

    def get_name (self):
        return self.__name