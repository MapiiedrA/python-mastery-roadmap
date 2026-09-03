### Conditionals ###

my_condition = False  #Mi condicion debe ser true or falsa, y eso va afectar la siguiente linea, ya que es la condicion if 

if my_condition:
    print("Se ejecuta la condicion del if") #la condicion del if de complicar para que salga. es lo mismo que "if my_condition = True"


my_condition = 5 * 5  #True

if my_condition == 10: #Se obliga a comprobar algo en concreto para que la condicion sea True
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25") #si esta condicion no se cumple realiza esta otra opcion.


print("La ejecucion continua")

my_string = ""

if not my_string:
    print("Mi Cadena de Texto es vacia")

