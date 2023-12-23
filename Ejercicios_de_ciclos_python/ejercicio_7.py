
#Escribir un programa que muestre por pantalla la tabla demultiplicar del 1 HASTA EL 10 en 1 al 10.
total=0
for i in range (0,11):
    print("tabla de multiplicacion del numero",i)
    for f in range(0,11):
        total=i*f
        print(i,"*",f,"=",total)
        
    