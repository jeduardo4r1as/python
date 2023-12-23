from datetime import datetime

class validar_edad:

#Escribir un programa que pregunte al usuario su edad y
#  muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)
   
   def edad_cumplida(self, edad):

    fecha_actual=datetime.now().year
    
    edad_cumple=fecha_actual-edad
    
    for i in range(edad_cumple,fecha_actual):

        
        print("Has cumplido años en los siguientes años:",i)



fecha_cumpleanos=validar_edad()

print('ingrese tu edad')
    
numero=int(input("¿Que edad tienes?"))
fecha_cumpleanos.edad_cumplida(numero)