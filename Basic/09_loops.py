### Loops ### 

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es Opcional
    print("Mi Condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:  #el loop se va cumplir mientras la condicion de <20 se cumpla # while se va ejecutar en funcion de una operacion.
    my_condition += 1
    if my_condition == 15:
        print("Se Detiene la Ejecucion")
        break
    print(my_condition)

print()

# For  #Nos sirve para iterar un listado de elementos

my_list = [35, 24, 62, 52, 30 , 30, 17]

for element in my_list:  #For se va ejecutar en funcion de la cantidad de elementos que tenga.
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:  
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:  
    print(element)

my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35}

for element in my_dict:  
    print(element)
    if element == "Apellido":
        continue  #Con esto podemos decirle que sea capaz de ejectutar algo o revisar algo. # El continue regresar al for y luego sigue donde quedo anteriormente. #"continue" y "go to" no suele ser muy comun en lenguajes modernos.
    print("Se Ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")

for element in my_dict:  
    print(element)
    if element == "Apellido":
        break #acaba con el for , pero puede seguir con lo que este fuera del scope.