### Dictionaries ###

my_dict = dict()
my_other_dict = {} #version corta de Dicts

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "Mauricio", "Apellido":"Piedra", "Edad":32, 1:"Python"}

my_dict = {
    "Nombre" : "Mauricio",                           #esto cuando queda como colugnas hacia abajo se llama formateo
    "Apellido":"Piedra",                                #un diccionario es un tipo de estructura donde podemos almacenar datos de tipo valor, se pueden consultar los valores por clave valor.
    "Edad":32, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.69
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))          #dicts es muy parecido a Json.
print(len(my_dict))      

print(my_dict["Nombre"]) #imprime la clave valor nombre, los dicts tienen una facilidad para acceder a un elemento.

my_dict["Nombre"] = "Pedro"   #si accedemos a esta clave y la igualamos con nuevo valor clave, la estamos actualizando. Cambia el antiguo valor por uno nuevo.
print(my_dict["Nombre"]) 

print(my_dict[1]) 

my_dict["Calle"] = "Calle MapiiedrA" #esta es la forma de agregar un nuevo valor a nuestro diccionario.
print(my_dict)

del my_dict["Calle"] #esta es la forma de borrar un solo elemento de un Dict.
print(my_dict)

print("Piedra" in my_dict) #da False , porque nosotros estamos buscando CLAVE VALOR, no el item dentro del diccionario.
print("Apellido" in my_dict) #Da True ya que la Clave valor si existe en el dict.
#print("Piedre" in my_dict)
print(my_dict["Apellido"]) #esta la forma de obtener un valor en concreto dentro del Dict.

print(my_dict.items()) #Genera un listado de cada uno de los items.
print(my_dict.keys()) #solo nos retorna un listado de keys
print(my_dict.values()) #nos retorna todos los valores
#print(my_dict.fromkeys(("Nombre", 1))) 

my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso")) #lo que hace es crear un dict sin valores , los nuevos valores de Cero.
print(my_new_dict)

#my_new_dict = dict.fromkeys("Nombre", 1, "Piso")  #esto no es habitual

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys((my_dict)) #creamos un nuevo dict desde cero, pero se ha quedado solo con las claves, ya solo queda llenarlos con datos.
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Mauricio", "Piedra")) #le metimos a todos los elementos los valores.
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, ["Mauricio", "Piedra"]) #le metimos a todos los elementos los valores.
print((my_new_dict))   #esto y lo anterior no tiene sentido, desde my list. curiosidad

print(my_new_dict.values())
print(list(my_new_dict)) #esto imprime las claves pero no los valores.
print(tuple(my_new_dict)) #en otro lenguajes mas typados esto daria error Los 2 ejemplos 
print(set(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))
print(list(my_new_dict.values()))
print(list(dict.fromkeys(list(my_other_dict.values())))) #esto como crear un nuevo dict pero dando mas vueltas. es demasiado rebuscado para ser util.
print(list(dict.fromkeys(list(my_other_dict.keys())))) ##
print(list(dict.fromkeys(list(my_other_dict.values())).keys())) #es demasiado rebuscado para ser util.

