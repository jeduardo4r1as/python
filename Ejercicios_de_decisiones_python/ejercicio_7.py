 # Definimos dos variables llamadas maquina y
# usuario, y asociaremos un número a cada una para comparar y determinar el ganador o empate
import random
maquina= random.randint(1, 3)

usuario  = int(input("¿Que selecion vas a escoger 1.piedra 2.pepel o 3.tijera ?"))

eleusuario=""
elemaquina=""

# como la opcion de la maquina y el usuario van hacer numeros se crea una variable string
#para que la eleccion quede guarda con una descripcion  piedra va hacer 1 papel va hacer 2 tijera va hacer 3
if maquina==1:
   elemaquina="piedra"

elif  maquina==2:
     elemaquina="papel"
elif  maquina==3:
      elemaquina="tijera"

if usuario==1:
    eleusuario="piedra"
elif  usuario==2:
     eleusuario="papel"
elif  usuario==3:
      eleusuario="tijera"


# piedra va hacer 1 papel va hacer 2 tijera va hacer 3

if maquina==usuario :
    print("Empate la maquina y el usuario escogieron la misma opcion")
    print("seleccion del usuario es:  " + eleusuario)
    print("seleccion de la maquina es: "+ elemaquina)

elif  maquina==1 and usuario==3 or maquina==2 and  usuario==1 or maquina==3 and usuario==2:
    print("Maquina gana")
    print("seleccion del usuario es:  " + eleusuario)
    print("seleccion de la maquina es: "+ elemaquina)

elif  usuario==1 and maquina==3 or usuario==2 and maquina==1 or usuario==3 and maquina==2:
     print("Usuario gana")
     print("seleccion del usuario es:  " + eleusuario)
     print("seleccion de la maquina es: "+ elemaquina)

print("************************************************")
print("seleccion del usuario es:  " + str(usuario))
print("seleccion de la maquina es: "+ str(maquina) )