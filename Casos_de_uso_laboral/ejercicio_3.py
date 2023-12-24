import time
#Hacer un conteo regresivo desde hora, minuto y segundos

while True:

    tiempo_actual=time.localtime()

    horas=tiempo_actual.tm_hour
    minutos=tiempo_actual.tm_min
    segundos=tiempo_actual.tm_sec


    print(f"{horas:02}:{minutos}:{segundos}", end="\r")
    time.sleep(1)