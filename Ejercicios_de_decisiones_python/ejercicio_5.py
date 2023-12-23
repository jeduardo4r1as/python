#Realizar un software que detecte si el número que me ingreso el usuario es
#  un múltiplo de 3 y también que sea par.

print('ingrese un número para que se detecte si el número que me ingreso el  usuario es un numero par  y que sea multiplo de 3')
    
numeroentero=int(input("¿Que numero va a ingresar?"))

if numeroentero % 3 == 0:
  print('el numero que ingreso es multiplo de tres:',numeroentero)

  if numeroentero % 2 == 0:
     print('el numero que ingreso es numero par:',numeroentero)
      
  else:
     print('el numero que ingreso es impar:',numeroentero)

else:
  print('el numero que ingreso no es multiplo de 3')
  if numeroentero % 2 == 0:
     print('el numero que ingreso es numero par:',numeroentero)
      
  else:
     print('el numero que ingreso es impar:',numeroentero)
