class validacion_numero:
#Validar que un usuario ingrese un número positivo (mayor que cero)
    
    def validar_numero(self, numero):

        if numero>0:
            print('El numero ingresado si es positivo',numero)
            return True
        else:
          print('El numero ingresado no es positivo',numero)
          return False

numero_usuario=validacion_numero()
   
while True:
 
 
 print('ingrese un número positivo (mayor que cero)')
    
 numero=int(input("¿Que numero va a ingresar?"))

 validacion=numero_usuario.validar_numero(numero)

 if  validacion :
    break
  