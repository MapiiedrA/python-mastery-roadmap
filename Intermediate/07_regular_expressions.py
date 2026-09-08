### Regular Expressions ### sirve para comprobar si una cadena de texto tiene cosas.

import re 

# match

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string, re.I) #re.I = Significa ignore case
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la leccion", my_other_string)
#if not (match == None): # Otra forma de comprobar el None
#if match is not None: # Otra forma de comprobar el None
if match != None: # not es igual a != None
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string)) #Match empieza a buscar desde el principio sino retorna None

# search

search = re.search("leccion", my_string, re.I) #busque el elemento en cualquier sitio de la cadena de texto, pero solo la primera vez que aparece
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string, re.I) #hace un listado de cantidad de veces que encuentra el elemento
print(findall)

# split # sirve para dividir , busca un patron y divide en ese lugar, previamente asignado

print(re.split(":", my_string))

# sub ##sirva para sustituir

print(re.sub("[L|l]]eccion", "LECCION", my_string))
print(re.sub("leccion|Leccion", "LECCION", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patterns   #estos patrones se puede usar para validar > ejemplo Emails, numeros telefonicos o Nombres

pattern = r"[Ll]eccion"
print(re.findall(pattern, my_string))

pattern = r"[Ll]eccion|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"  #Busca todas las letras de a - z
print(re.findall(pattern, my_string))

pattern = r"[0-9]" #solo busca numeros
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"  #este ignora las letras y deja solo numeros
print(re.findall(pattern, my_string))

pattern = r"\D" #este ignora numeros y deja solo Letras
print(re.findall(pattern, my_string))

pattern = r"[l]."  #busca coincidencias con la letra ejemplo la L
print(re.findall(pattern, my_string))

pattern = r"[l].*"   #Busca coincidencia L hacia adelante, o todo el texto luego de la L , puede ser otro valor L es para el ejemplo
print(re.findall(pattern, my_string)) 

# ejemplo de Email Validation

email = "mapiedra3223@gmail.com"
#def is_valid_email(email):
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"  #esta es la regla de comprobacion
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))
#return re.match(pattern, email)

email = "mapiedra3223@gmail"   #tambien se podria agregar un filtro de dominios al email
print(re.findall(pattern, email))