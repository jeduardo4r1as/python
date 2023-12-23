#Realizar un software que detecte si el número que me ingreso el 
# usuario es un numero negativo y que sea par.

print('ingrese un número negativo  detecte si el número que me ingreso el  usuario es un numero negativo y que sea par')
    
numeroentero=int(input("¿Que numero va a ingresar?"))

if numeroentero<0:
  print('el numero que ingreso es negativo')

  if numeroentero % 2 == 0:
     print('el numero que ingreso es numero par:',numeroentero)
      
  else:
     print('el numero que ingreso es impar:',numeroentero)

else:
  print('el numero que ingreso es positivo')
  if numeroentero % 2 == 0:
     print('el numero que ingreso es numero par:',numeroentero)
      
  else:
     print('el numero que ingreso es impar:',numeroentero)
