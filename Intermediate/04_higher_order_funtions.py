### Higher Order Functions ### Son Funciones que pueden llamar a otro funcion.

def sum_one(value): #Function 
    return value + 1

def sum_five(value): #Function
    return value + 5

def sum_two_values_and_addone(first_value, second_value, f_sum): #Para interpretacion, esto suma los 2 valores suministrados, y luego hagace un return de f_sum como function, que comprende la suma de ambos antes de las primeras functions.
    return f_sum(first_value + second_value)

print(sum_two_values_and_addone(5, 2, sum_one))
print(sum_two_values_and_addone(5, 2, sum_five))

### Clousures ###  se usa para hacer return de funciones

def sum_ten():
    def add(value):
        return value + 10
    return add 

add_clousure = sum_ten()
print(add_clousure(5))

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value #este original_value equivale ala referencia de 5+10 = 15 + original_value(+3)=18 
    return add 

add_clousure = sum_ten(3) #esto es el acceso al add
print(add_clousure(5))
print((sum_ten(5))(3))  #esto son llamadas ala funciones.

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers))) #este map siempre va necesitar una lista o un conjunto de iterables, luego a iterado cada uno de los valores que tenemos y ejecutado sobre cada valor la function que definimos.
print(list(map(lambda number: number * 2, numbers))) #esto ya con una lambda, es mejor crear lambdas que functions cuando hay un scope limitado.

### Filter ### Sirve para filtrar valores intinerados

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers))) #este print va hacer lo mismo que el filter en este caso.

### Reduce ###

from functools import reduce # no es una función integrada disponible directamente. Debes importarla desde "functools" y pasarle una función acumuladora y el iterable

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))