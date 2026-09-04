### Error Types ### Excepciones propias de Python

# SyntaxError

#print "Hola Comunidad!" #Descomentar para Error 
print("Hola Comunidad!")

# NameError
language = "Spanish" #Comentar para Error en la siguente linea
print(language) #Error, ya que no hay variable definida.

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[-1])#recorre la lista desde el final
print(my_list[0])
print(my_list[4]) 
#print(my_list[5])#Descomentar para Error, index out of range

# ModuleNotFoundError
#import maths #Descomentar para Error, No module named 'maths'
import math

# AttributeError
#print(math.PI) #Descomentar para Error, module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) #Descomentar para Error, KeyError: 'Apelido'
print(my_dict["Apellido"])

# TypeError
#print(my_list["0"]) #Descomentar para Error, TypeError: list indices must be integers or slices, not str.
print(my_list[0])
print(my_list[False]) #Curiosidad tambien se puede acceder como boolean, pero porque se traduce False = 0, igual no tiene utilidad.
print(my_list[True])  #Curiosidad tambien se puede acceder como boolean, pero porque se traduce True = 1, igual no tiene utilidad.

# ImportError
#from math import PI # Descomentar para Error, ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)

# ValueError
#my_int = int("10 Años") # Descomentar para Error, ValueError: invalid literal for int() with base 10: '10 Años'
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para Error, ZeroDivisionError: division by zero
print(4/2)