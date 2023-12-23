class numero_multiplo7:

#Realizar un software que detecte si el número que me ingreso el usuario es
#  un múltiplo de 7 y también que sea par.

    def validar_numero(self, numero):

       if numeroentero % 7 == 0:
          print('el numero que ingreso es multiplo de 7:',numeroentero)

          if numeroentero % 2 == 0:
             print('el numero que ingreso es numero par:',numeroentero)
      
          else:
              print('el numero que ingreso es impar:',numeroentero)

       else:
            print('el numero que ingreso no es multiplo de 7')
            if numeroentero % 2 == 0:
              print('el numero que ingreso es numero par:',numeroentero)
      
            else:
               print('el numero que ingreso es impar:',numeroentero)



print('ingrese un número negativo  detecte si el número que me ingreso el  usuario es un numero negativo y que sea par')
    
numeroentero=int(input("¿Que numero va a ingresar?"))

validarmultiplo7=numero_multiplo7()

validarmultiplo7.validar_numero(numeroentero)