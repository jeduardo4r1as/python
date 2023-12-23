class menu:

#Realizar un software en donde sea un menú combos en un restaurante con cada 
# uno de sus contenidos, ejemplo: 1. Combo de hamburguesas de carne al horno con jugo de 
# coco; en donde se muestre la información de lo que el usuario va a a consumir
#  para el usuario dependiendo del numero que digite el usuario.
  def combo(self, numerocombo):

   if numerocombo==1:
    print('Combo 1 hamburguesas de carne al horno con jugo de coco')
   elif  numerocombo==2:
     print('2.Combo 2 Perro caliente con tocineta y limonada natural')
   elif  numerocombo==3:
      print('3.Combo 3 pizza  con peperoni con gaseosa')
   elif  numerocombo==4:
      print('4.Combo 4 salchipapa con queso tocineta costilla y jugo de mora')
   


seleccioncombo=menu()

print('ingrese el numero del combo que desea  escoger')
print('1.Combo 1 hamburguesas de carne al horno con jugo de coco')
print('2.Combo 2 Perro caliente con tocineta y limonada natural')
print('3.Combo 3 pizza  con peperoni con gaseosa')
print('4.Combo 4 salchipapa con queso tocineta costilla y jugo de mora')
    
numeroentero=int(input("¿Que numero va a ingresar?"))

seleccioncombo.combo(numeroentero)