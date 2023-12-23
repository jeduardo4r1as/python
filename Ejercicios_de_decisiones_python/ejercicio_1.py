class validar_numeroprimo:
#Realizar un software que detecte si el número que me ingreso el usuario es 
# número par y validar que es múltiplo de 6.
    def  validar_numero(self, numero):

        if numero % 2 == 0:
            print('el numero que ingreso es numero par:',numero)
            if numero % 6 == 0:
                 print('el numero que ingreso es mutiplo de 6:',numero)
            else:
                print('el numero que ingreso no es mutiplo de 6:',numero)
        else:
            print('el numero que ingreso es impar:',numero)


validacion=validar_numeroprimo()

print('ingrese un número positivo (mayor que cero) para determinar si es par')
    
numeropar=int(input("¿Que numero va a ingresar?"))

validacion.validar_numero(numeropar)

