### File Hadling ###

import os

# .txt file
txt_file = open("./my_file.txt", "w+") #Leer , escribir y sobreescribir si ya existe.
#txt_file.write("Mi nombre es Mauricio\nMi apellido es Gutierrez\nTengo 32 años\nMi lenguaje preferido es Python")
#txt_file = open("./my_file.txt", "r+")  # Leer y escribir

#print(txt_file.read())
print(txt_file.read(10)) #solo lee las primeras 10 letras del fichero
print(txt_file.readline()) #Lectura linea a linea
print(txt_file.readlines()) #Le todas las lineas, pone un salto de linea al final de cada una
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta Javascript")
print(txt_file.readline())

txt_file.close()

with open("./my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Go")

#os.remove("./my_file.txt") sirve para borrar el fichero

# .json file 

import json

json_file = open("./my_file.json", "w+")

json_test = {
    "name" : "Mauricio", 
    "surname":"Piedra", 
    "age":32, 
    "lenguages":["Python", "Javascript", "Go"], 
    "nickname":"MapiiedrA"}

json.dump(json_test, json_file, indent=2) #la indent varia segun el tamaño del fichero, sin indent queda todo en una linea. Indent: es la cantidad de espacios por delante de cada linea
#json.dump(json_test, json_file, indent=2)si ponemos esto otra vez, vuelve a escribir lo mismo al final del .json

json_file.close()

with open("./my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("./my_file.csv", "w+") #es como una tabla de datos. como excel pero no es un excel

csv_writer= csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "nickname"])
csv_writer.writerow(["Mauricio", "Piedra", 32, "Python", "MapiiedrA"])
csv_writer.writerow(["Rosswell", "Bot", 1, "Python", "Music"])

csv_file.close

with open("./my_file.csv") as my_other_file:
    for line in my_other_file.readline():
        print(line)

# .xlsx file
#import xlrd # se necesita instalar modulo

#.xml file

import xml