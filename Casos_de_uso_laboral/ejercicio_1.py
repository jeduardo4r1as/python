class universidad:

#Están realizando un software educativo universitario en donde se
#  necesita que cuando el se ingrese la nota (del 0 hasta el 5,0), 
# si es 0 hasta el 0,9 entonces perdió la materia sin poder recuperar
#  y se da un mensaje: “Perdida la materia en (Pone la nota) sin tener
#  recuperación”. Si es 1,0 hasta el 2,5 entonces perdió la materia, 
# pero puede recuperar y si saca la nota máxima en la habilitación que
#  es 5,0 en la recuperación, su nota final es 3.0 con un mensaje “Perdido
#  la materia en (pone la nota) pero se puede nivelar máximo nota final 3.0”. 
# Si es 2,6 hasta 2,9, se puede recuperar y si saca la nota máxima en la habilitación
#  que es 5,0 en la recuperación, su nota final es 3.5 con un mensaje “Perdido la materia
#  en: (pone la nota) pero se puede nivelar máximo nota final 3.5”. Si ya es 3.0 a 3.5 pero
#  nivelado, mensaje: “Aceptable: (Pone la nota) por recuperación”. 3.0 hasta 3.9 sin recuperación,
#  mensaje: “Aceptable: (Pone la nota), te recomiendo que sigas mejorando, vas bien”. 4.0 hasta 4.5,
#  mensaje: “Excelente: (Pone la nota), vas por un buen camino hacia el éxito”. 4.5 hasta 5.0 mensaje, 
# “Científico: (Pone la nota) tienes un gran futuro adelante”

    def calificacionestudiante(self,nota):

      if nota>=0 and nota<=0.9:
        print('perdió la materia sin poder recuperar Perdida la materia en:',nota,'sin tener recuperación')
      elif  nota>=1.0 and nota<=2.5:

        print('Perdido la materia en:',nota,'pero se puede nivelar máximo nota final 3.0')
        
        print('ingrese  la nota que saco  en la habilitación')
    
        habilitacion=int(input("¿Que nota de habilitación va a ingresar?"))
        if habilitacion==5:
            print('gano la materia nota final 3.0')
        elif  habilitacion<5:
            print('Perdido la materia ya que la nota de la habilitacion no alcanza para nivelar')

      elif  nota>=2.6 and nota<=2.9:
        print('verdura se le ofrecerá agua')
        print('ingrese  la nota que saco  en la habilitación')
    
        habilitacion=int(input("¿Que nota va a ingresar?"))
        if habilitacion==5:
            print('gano la materia nota final 3.5')
        elif  habilitacion<5:
            print('Perdido la materia ya que la nota de la habilitacion no alcanza para nivelar tenia que ser igual a cinco')
      elif  nota>=3.0 and nota<=3.9:
        print('Aceptable: ',nota,'gano la materia te recomiendo que sigas mejorando')
      elif  nota>=4.0 and nota<=4.5:
        print('“Excelente:',nota,', vas por un buen camino hacia el éxito')
      elif  nota>=4.6 and nota<=5.0:
        print('Científico:',nota,'tienes un gran futuro adelante')

curso=universidad()

while True:

  print('En el siguiente menu ingrese  la nopcion que desees realizar')

  opcion=int(input('1. Ingresar nota para validar si gano materia 2.SALIR'))



  if opcion==1:
      nota=int(input("¿Que nota  va a ingresar?"))
      curso.calificacionestudiante(nota)
  elif opcion==2 :
    print('gracias por utilizar la aplicacion adios')
    break


