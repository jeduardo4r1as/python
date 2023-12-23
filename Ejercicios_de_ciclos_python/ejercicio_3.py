class validacion_numero:
#Algoritmo que valide que un usuario ingrese un número positivo de 3 cifras
    
    def validar_numero(self, numero):

        if numero>=100:
            print('El numero ingresado si es positivo y es mayor a 100 numero ingresado:',numero)
            return True
        else:
          print('El numero ingresado no es positivo o es menor a 100 numero ingresado:',numero)
          return False

numero_usuario=validacion_numero()
   
while True:
 
 
 print('ingrese un número positivo de 3 cifras')
    
 numero=int(input("¿Que numero va a ingresar?"))

 validacion=numero_usuario.validar_numero(numero)

 if  validacion :
    break
  