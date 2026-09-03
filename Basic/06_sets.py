### Sets ###

my_set = set()
my_other_set = {} #inicialmente es un diccionario #Curiosidad*.

print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario #Curiosidad*.

my_other_set = {"Mauricio", "Piedra", 32}
print(type(my_other_set))

print(len(my_other_set))

"""
print(my_other_set[0]) #TypeError: 'set' object is not subscriptable, pero no aplica aqui -[?] para acceder a los datos dentro de la variable, puede ser en cualquier tipo de Constructor variable.
"""

my_other_set.add("MapiiedrA")  #un set no es una estructura ordenada, no funciona como un listado.
print(my_other_set) 

my_other_set.add("MapiiedrA") #un set no admite repetidos.
print(my_other_set)

print("MapiiedrA" in my_other_set) #sirve para comprobar si existe un valor dentro del set
print("MapyyedrA" in my_other_set) #sirve para realizar busquedas tambien, dentro del mismo set.

my_other_set.remove("MapiiedrA") #Se puede eliminar datos
print(my_other_set)

my_other_set.clear() #sirve para limpiar el set , sin borrarlo del todo. #las acciones propias de un conjunto accedemos por un "." o un "Punto"
print(my_other_set)
print(len(my_other_set))

del my_other_set  #Borramos el set completamente el objeto, DEL es una funcion propia de Python no del conjunto. 
#print(my_other_set) #NameError: name 'my_other_set' is not defined

my_set= {"Mauricio", "Piedra", 32}
my_list = list(my_set) #converti el set en una lista
print(my_list)
print(my_list[0]) #aunque hagamos esto no vamos conocer el orden del set

my_other_set = {"switf", "Bash", "Python"}

my_new_set = my_set.union(my_other_set) 
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) #sirve para unir elementos en para una variable, pero solo para una ejecucion en especifico, no modifica la variables al ir entre {}.
print(my_new_set)
print(my_new_set.difference(my_set)) #sirve para diferenciar los elementos de un set.

