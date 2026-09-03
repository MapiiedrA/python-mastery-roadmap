### Lists ###

my_list = list() #sirve para crear estructura de datos. #el primer my_list es para lista, segundo es un objecto. ambos listas.
my_other_list = [] 

print(len(my_list)) #en la lista entrar en posicion cero siendo el primero item.

my_list = [32, 24, 62, 30, 17, 52, 32]  #no hay problema si se repite el mismo valor

print(my_list)
print(len(my_list))

my_other_list = [32, 1.69, "Mauricio", "Piedra"]

print(type(my_list)) 
print(type(my_other_list))

print(my_other_list[1]) #numero 1 ya que 32 es el segundo en lista, porque el primero es cero. Range on my list [0 a 3].
print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
#print(my_other_list[-5]) #IndexError: list index out of range, ya que no hay ningun elemento en esa posicion
#print(my_other_list[4])  #IndexError
print(my_other_list.count("Mauricio"))
print(my_list.count("32")) #es para ver cuantas veces se repite.

print(my_other_list.index("Mauricio")) #sirve para ver un Indice en la lista.

age, height, name, surname = my_other_list #el orden de la variable tiene que consistir con el orden de los valores.
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1],  my_other_list[0], my_other_list[3] #sirve tambien pero es forma muy complicada y no suele tener sentido, da pie a muchos errores.

print(name)
print(age)

print(my_list + my_other_list) #tambien se puede concatenar 2 listas o mas.
print(list[1, 2, 3, 4]) #tambien se puede pero solo va imprimir los nuevos valores de esta lista.
#print(my_list - my_other_list) Index Error

my_other_list.append("MapiiedrA") #append puede insertar un nuevo valor en la lista ya sea al final.
print(my_other_list)

my_other_list.insert(1, "Red") #insert puede insertar un nuevo valor en la posicion en especifico
print(my_other_list)

my_other_list[1] = "Cyan" #sirve para acceder un valor en especifico y cambiarlo.

my_other_list.remove("Cyan") #sirve para remover un valor de la lista
print(my_other_list)

my_list.remove(32) #Remove remuve el primero que ha encontrado en la lista.
print(my_list)

my_list.pop() #Quita el ultimo valor de la lista por Defecto. nos devuelve el valor que hemos apilado.
print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2) #Guarda el valor en una variable especifica luego de eliminarlo.
print(my_pop_element)
print(my_list)

del my_list[1] #Del elimina por indice.
print(my_list)

my_new_list = my_list.copy() #sirve para copiar la lista en una nueva variable, en la linea en especifico, asi se borre la lista Original posterior al copy.

my_list.clear() #sirve para limpiar la lista.
print(my_list)
print(my_new_list)

my_new_list.reverse() #sirve para revertir los valores de la lista, despues de un cambio.
print(my_new_list)

my_new_list.sort() #criterios para ordenar un lista, por default ordena de mayor a menor en caso de numeros.
print(my_new_list)

print(my_new_list[1:3]) #sirve para crear sub listas conociendo el valor de item.

my_list = "Hola Python" #si lo dejamos con comillas la lista pasa a ser un "str" pero si le ponemos [] vuelve a ser una lista, ya que lo definimos asi, incluso: list("Hola Python") tambien podria ser una lista.
print(my_list) 
print(type(my_list)) 
