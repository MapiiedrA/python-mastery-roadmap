### Exceptions Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

#try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")

#try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")

#try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #else y finally son opcionales.
    print("La ejecucion continua correctamente")
finally: #Se ejecuta siempre pase lo que pase
    print("La ejecucion continua")

#Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

#Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)