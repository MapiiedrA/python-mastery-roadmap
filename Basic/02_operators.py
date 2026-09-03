### Operators ###

#ejemplo de operadores aritmeticos

print(3 + 4) #Suma  
print(3 - 4) #Resta
print(3 * 4) #Multiplicacion
print(3 / 4) #Division, devuelve un numero decimal
print(10 % 3) #Operador modulo, devuelve el residuo de la division
print(10 // 3) #Division con resultado aproximado entero
print(2 ** 3) #Potencia
print(2 ** 3 + 3 - 7 / 1 // 4) #Se pueden combinar varios operadores en una sola expresion, siguiendo el orden de precedencia de los operadores

6 + 10 #Sin Print no se ejecuta en la terminal

print("Hola" + "Python") #Se puede usar el operador + para concatenar cadenas de texto
###print("Hola" - "Python") #No se puede restar cadenas de texto, sino da Error  
print("Hola" + "Python" + "Que Pasa") #Se pueden concatenar varias cadenas de texto
print("Hola" + str(5)) #Se puede concatenar una cadena de texto con un numero entero, pero primero hay que convertir el numero a cadena de texto con la funcion str()
print("Hola" * 5) #Se puede multiplicar una cadena de texto por un numero entero, para repetirla varias veces
print("Hola" + "Python" * 5) #Se puede multiplicar una cadena de texto por un numero entero, para repetirla varias veces
print("Hola" * (2**3)) #Se puede multiplicar una cadena de texto por un numero entero, para repetirla varias veces
###print("Hola" * 2.5) #No se puede multiplicar una cadena de texto por un numero decimal, sino da Error

my_float = 2.5 * 2 #Se puede multiplicar un numero decimal por otro numero decimal, y el resultado es un numero decimal
print("Hola" * int(my_float)) #Se puede multiplicar una cadena de texto por un numero decimal, pero primero hay que convertir el numero a entero con la funcion int()

### Operadores de comparacion (Bool)###
print(3 > 4) #Mayor que
print(3 < 4) #Menor que
print(3 >= 4) #Mayor o igual que
print(3 <= 4) #Menor o igual que
print(4 >= 4) #Igualados
print(3 == 4) #Igual que
print(3 != 4) #Distinto de
print(3 > 4 == 2) #Alt 6+2 Mayor Q, Alt 6+0 Menor Que
print(3 > 4 > 2) 

#Prueba
print("Hola" > "Python") #Se puede comparar cadenas de texto, pero se comparan por el orden alfabetico, y no por el significado de las palabras
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print("Hola" > "Bola") #True por orden alfabetico, H es mayor que B
print ("Hola" < "Bola") #False por orden alfabetico, H es mayor que B
print("Hola" >= "Bola") 
print(len("aaaa")>= len("abaa")) #Cuenta la cantidad de caracteres de cada cadena de texto y compara los resultados #True, 4 es mayor que 4, pero como es mayor o igual que, devuelve True #Basado en ASCII 
print(len("AAAA")<= len("ABAA")) #Cuenta la cantidad de caracteres de cada cadena de texto y compara los resultados #True, 4 es menor que 4, pero como es menor o igual que, devuelve True #Basado en ASCII

#### Operadores logicos (Bool) ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")#Seguira siendo true, porque siempre hay un true en la expresion
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) #True, porque hay un true en la expresion #el "OR" va afectar lo que esta en el parentesis
#print(3 > 4 not (3 > 4)) #no es un operador valido, sino da error
print(not (3 > 4)) #Not se usa para negar una expresion, en este caso, 3 > 4 es False, pero al negarlo con not, devuelve True

#Logica Booleana Explicada "La lógica booleana es un sistema matemático de valores binarios que utiliza los estados verdadero (1) y falso (0), operando mediante las funciones lógicas básicas AND (Y), OR (O) y NOT (NO)."
"""""
Logica Booleana AND
A	B	A AND B  
0	0	0
0	1	0
1	0	0
1	1	1
"""
"""
Logica Booleana OR 
A	B	A OR B
0	0	0
0	1	1
1	0	1
1	1	1
"""
"""
NOT(Negacion logica)
A	NOT A
0	1
1	0
"""