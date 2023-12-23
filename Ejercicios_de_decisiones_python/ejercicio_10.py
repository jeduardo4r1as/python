class juegos:

#En una sala de juegos existen tre salas: Consolas, Juegos 2D, Juegos 3D, Realidad Virtual. Si 
# un usuario paga 4 créditos puede acceder a todas, si apga 3 solo podrá acceder a 
# las tres primeras, si paga 2 a las dos primeras y si paga 1 solo a la primera sala.

  def combo(self, numerocombo):

   if numerocombo==4:
    print('pagaste 4 créditos puedes acceder a Consolas, Juegos 2D, Juegos 3D, Realidad Virtual')
   elif  numerocombo==3:
     print('pagaste 3 créditos solo podes acceder a las tres primeras Consolas, Juegos 2D, Juegos 3D')
   elif  numerocombo==2:
      print('pagaste  2  créditos puedes acceder a las dos primeras Consolas, Juegos 2D')
   elif  numerocombo==1:
      print('pagaste 1 credito solo a la primera sala puedes acceder')
 
   


seleccioncombo=juegos()

print('ingrese el numero de fichas para Consolas, Juegos 2D, Juegos 3D, Realidad Virtual. ')    
print('paga 4 créditos puede acceder a todas, ')   
print('paga 3 solo podrá acceder a las tres primeras')   
print('paga 2 a las dos primeras')   
print('paga 1 solo a la primera sala.')   
numeroentero=int(input("¿Que numero de fichas  va a ingresar?"))

seleccioncombo.combo(numeroentero)