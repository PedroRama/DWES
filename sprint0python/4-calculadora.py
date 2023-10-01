repetir = 's'

while repetir == 's':

    numero1 = int (input ("Escribe el primer numero"))
    numero2 = int (input ("Escribe el segundo numero"))

    print ("Que quieres hacer?:")
    operacion = input ("a.suma, b.resta, c.multiplicación, d.división")

    if (operacion == 'a'):

        resultado = numero1 + numero2

        print ("el resultado final es:" +str(resultado))

    if (operacion == 'b'):
   
        resultado = numero1 - numero2

        print ("el resultado final es:" +str(resultado))

    if (operacion == 'c'):
   
        resultado = numero1 * numero2

        print ("el resultado final es:" +str(resultado))

    if (operacion == 'd'):

        try:

            if numero1 == 0 or numero2 == 0:
                print("No se puede dividir por cero.")
            else:
                resultado = numero1 / numero2
                print ("el resultado final es:" +str(resultado))

        except:

            print("Numeros no válidos")

    repetir = input ("Si quieres hacer otra operacion escribe s")