### Dates ###   #Formato POSIX 

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
 
year_2027 = datetime(2026, 9, 3, 5)#Lo minimo que nos va pedir es año, mes y dia, pero podemos agregarle hora, minuto y segundo

print_date(year_2027)

from datetime import time

current_time = time(15, 30, 45) #hora, minuto y segundo
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today() #año, mes y dia
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday()) #0 es lunes, 6 es domingo

current_date = date(2026, 9, 3) #Definimos una fecha en especifico, año, mes y dia
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_time = time.fromisoformat('15:30:45') #hora, minuto y segundo
print(current_time.hour)

current_date = date(current_date.year, current_date.month + 1, current_date.day) #Definimos una fecha en especifico, sin agregar hora, minuto y segundo. y sumarle +1
print(current_date.month)

diff = year_2027 - now 
print(diff)
diff = year_2027.date() - current_date #Restamos dos fechas y nos devuelve un objeto timedelta
print(diff) #Restamos dos fechas y nos devuelve un objeto timedelta
print(year_2027.time()) #Nos devuelve la hora de la fecha que le pasamos

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)#Definimos un intervalo de tiempo
end_timedelta = timedelta(365, 100, 100, weeks = 13) #Sirve para trabajar con limites de fechas, ejemplo suscripciones.
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

