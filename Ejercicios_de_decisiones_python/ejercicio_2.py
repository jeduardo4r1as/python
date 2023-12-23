class validar_numeroprimo:
#Realizar un software que detecte si el número que me ingreso el usuario es número impar y validar
#  que es múltiplo de 5.
    def  validar_numero(self, numero):

        if numero % 2 != 0:
            print('el numero que ingreso es numero impar:',numero)
            if numero % 5 == 0:
                 print('el numero que ingreso es mutiplo de 5:',numero)
            else:
                print('el numero que ingreso no es mutiplo de 5:',numero)
        else:
            print('el numero que ingreso es par:',numero)


validacion=validar_numeroprimo()

print('ingrese un número positivo (mayor que cero) para determinar si es impar')
    
numeropar=int(input("¿Que numero va a ingresar?"))

validacion.validar_numero(numeropar)

