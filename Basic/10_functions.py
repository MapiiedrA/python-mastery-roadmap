### Functions ###

def my_function (): 
    print("Esto es una Funcion") #Esta es la tarea de Funccion

my_function ()  #esto es la llamada de funcion

def sum_two_values (first_value, second_value): #Lo que esta dentro del parentesis son los parametros de funcion   
    print(first_value + second_value)  

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):  
    my_sum = first_value + second_value
    return my_sum

""""
my_result = sum_two_values(1.4, 5.2)   Curiosidad Resultado en consola va ser none
print(my_result)              
"""

my_result = sum_two_values_with_return (10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}") #con F de Formateo , accede a los valores dentro de llaves.

print_name(surname = "Piedra", name = "Mauricio")

def print_name_with_default (name, surname, alias = "Sin Alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Piedra", "Mauricio")
print_name_with_default("Piedra", "Mauricio", "MapiiedrA")

def print_texts(*text): #Puedo pasarle varios parametros por el * sin importar la cantidad , parametros del mismo tipo.
    print(text)

print_texts("Hola", "Python", "Mauricio")

def print_upper_texts(*texts): #Funcion con parametros arbitrarios y agregando que sean mayus.
    print(type(texts)) #A nivel de sistema python considera que la agrupacion de elementos de este tipo es una tuple
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Mauricio")
