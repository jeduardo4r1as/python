def imprimir_triangulo_rectangulo(altura):
    for i in range(1, altura + 1):
        print('* ' * i)


    altura = int(input("Ingresa un número entero para la altura del triángulo: "))
    if altura > 0:
        imprimir_triangulo_rectangulo(altura)
    else:
        print("Por favor, ingresa un número entero positivo.")
