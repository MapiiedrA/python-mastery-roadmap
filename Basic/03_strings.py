### Strings ###

my_string = "Mi String"
my_other_string = 'Mi String' #Es lo mismo las comillas simples y dobles, pero se recomienda usar comillas dobles para cadenas de texto y comillas simples para caracteres individuales

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) #Concatenacion de cadenas de texto

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\Este es un string \\n escapado"
print(my_scape_string)

# formateo de cadenas de texto

name, surname, age = "Mauricio", "Piedra", 30

print("Mi Nombres es {} {} y mi edad es {}" . format(name, surname, age)) # {} si estamos tirando datos
print("Mi Nombres es %s %s  y mi edad es %d" %(name, surname, age)) # %s para cadenas de texto y %d para numeros enteros #esta para formatear datos.
print(f"Mi Nombres es {name} {surname} y mi edad es {age}") #Forma mas eficiente #F es para formatear las variables
# *forma incorrecta de hacer el formateo -print("Mi Nombres es " + name + " " + surname + " y mi edad es " + str(age) #es funcional pero no es recomendable.

# Desempaquetado de Caracteres 
language = "Python"
a, b, c, d, e, f = language
print(a)
print(f)

""""
a, n = "Python" Forma incorrecta ya que son menos variables del total de la palabra completa o texto completo.
print(a)
print(b)
"""

#Division 

language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

language_slice = language [1:2:4]
print(language_slice)

language_slice = language [0:6:2] #usarlo para buscar solo las partes que queremos 
print(language_slice)

#Reverse 

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) #para ponerla primera en mayuscula
print(language.upper()) #mayusculas
print(language.count("t")) #cuantas letras tiene
print(language.count("y")) #cuantas letras tiene
print(language.isnumeric())
print("1".isnumeric())
print(language.lower()) #minisculas
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("Py")) #Inicia con ? - true or False #Pero recordar la Regla de ASCII mayusculas y minisculas influye.
print("Py" == "py") #No es lo mismo , mismo ejemplo de arriba, pero para entender las 2 formas. 