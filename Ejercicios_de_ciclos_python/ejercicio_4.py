class validar_numero:

#Realice un algoritmo que permita leer un número positivo. Luego indique si es un número perfecto.
#Nota: Un número es perfecto si la suma de sus divisores (sin incluir al mismo número) 
#resulta igual a sí mismo. Ejemplo: 6 es perfecto debido a que 6 = 1 + 2 + 3
    def validar_numero(self, numero):
      acumulador=0
      for  i  in range(1,numero):

        if numero%i ==0:

           acumulador=acumulador+i
     
      if acumulador==numero:

        print("********el numero es perfecto la suma de sus divisores (sin incluir al mismo número) resulta igual a sí mismo.***********")
        return True 
        
validacionperfecto=validar_numero()

while True:
 
 
 print('ingrese un número positivo (mayor que cero)')
    
 numero=int(input("¿Que numero va a ingresar?"))

 validacion=validacionperfecto.validar_numero(numero)

 if  validacion :
    break

     
