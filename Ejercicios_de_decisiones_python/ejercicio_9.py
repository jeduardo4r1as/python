class menu:

#En un restaurante los clientes pueden pedir menú de carne, pescado o verdura. Si pide 
# carne se le ofrecerá como bebida vino tinto, si pide pescado se le ofrecerá vino blanco
#  y si pide verdura se le ofrecerá agua. Si no elije el menú de la lista aparecerá 
# la frase elija carne, pescado o verdura.
  def combo(self, numerocombo):

   if numerocombo==1:
    print('carne se le ofrecerá como bebida vino tinto')
   elif  numerocombo==2:
     print('pescado se le ofrecerá vino blanco')
   elif  numerocombo==3:
      print('verdura se le ofrecerá agua')
 
   


seleccioncombo=menu()

print('ingrese el numero de la opcion  del  menú que desea  escoger')
print('1.carne')
print('2.pescado')
print('3.verdura.')

    
numeroentero=int(input("¿Que numero va a ingresar?"))

seleccioncombo.combo(numeroentero)