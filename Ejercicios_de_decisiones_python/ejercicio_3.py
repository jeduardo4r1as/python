
#Realizar un software que detecte si el número que me ingreso el usuario es un numero entero
#  no está permitidos números irracionales.

print('ingrese un número positivo (mayor que cero) para determinar si es numero entero no está permitidos números irracionales')
    
numeroentero=float(input("¿Que numero va a ingresar?"))


if numeroentero%1 == 0:
    print('el numero ingresado  es un numero entero ')
else:
    print('el numero ingresado  es un numero decimal ')