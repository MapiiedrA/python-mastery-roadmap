### TUPLES ###

my_tuple = tuple()  #las 2 Formas de definirlo. Lo que esta previo a Parentesis en este caso se llama constructor de clase.
my_other_tuple = ()

my_tuple = (32, 1.69, "Mauricio", "Piedra", "Mauricio")
my_other_tuple = (32, 60, 29)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) Index Error
#print(my_tuple[-6]) Index Error

print(my_tuple.count("Mauricio"))
print(my_tuple.index("Piedra"))
print(my_tuple.index("Mauricio"))

#my_tuple[1] = 1.80 #Error - no permite cambiar valores, ya que son inmutables con las tuplas* , tampoco deja insertar, ya que una tupla es inmutable. TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_tuple + my_other_tuple)

print(my_sum_tuple[3:6]) #slice

my_tuple = list(my_tuple) #con esto se puede convertir la tupla inmutable a mutable pero por el hecho de que ahora es una lista, osea cambia el tipo de datos.
print(type(my_tuple))  

my_tuple[4] = "MapiiedrA"
my_tuple.insert(1, "Cyan")
my_tuple = tuple(my_tuple ) # la reasignamos a tuple nuevamente para que vuelva a ser inmutable y mejoramos la seguridad, pero esto sirve para cambios muy en especifico que se requieran.
print(my_tuple)
print(type(my_tuple)) #<class 'tuple'> ahora si es nuevamente una tuple.

#del my_tuple[2] #TypeError: 'tuple' object doesn't support item deletion

del my_tuple #del borrar el tipo de dato, no le importa si es variable, tupla o lo que sea, ya que es una tarea propia del sistema. (no borra el contenido dentro, borra todo el tipo de dato).
#print(my_tuple) #NameError: name 'my_tuple' is not define