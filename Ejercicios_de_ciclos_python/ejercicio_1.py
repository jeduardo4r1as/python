
# Software que es una Tabla de multiplicar a partir de lo que le digite el numero. 
# Ejemplo: si digita el 2, entonces le muestra el programa la tabla del 2 desde el
#  1 hasta el10.


tabla_multiplicacion=int(input("¿Que tabla de multiplicacion desea ver con el numero que ingrese ?"))
contador=0
for i  in range(0,11):
  
   total=  tabla_multiplicacion *contador

   print("",tabla_multiplicacion,"*",contador,"=",total)

   contador=contador+1

   