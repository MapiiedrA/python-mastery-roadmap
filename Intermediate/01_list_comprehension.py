### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8) #Creamos una list con un rango, de hecho las mismas 3 listas son lo mismo en diferentes versiones, en principio.
print(list(my_range))

my_list = [i for i in range(8)] # i es palabra reservada.
print(my_list)

my_list = [i +1 for i in range(8)] #se puede hacer lo mismo con diferentes operaciones matematicas, /, *, - .
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number): #ejemplo con funciones.
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)

