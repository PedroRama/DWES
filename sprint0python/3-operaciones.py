print ("Que quieres hacer?:")
operacion = input ("a.suma, b.resta, c.multiplicación, d.división")

if (operacion == 'a'):
    numero1 = int (input ("Escribe el primer numero"))
    numero2 = int (input ("Escribe el segundo numero"))

    resultado = numero1 + numero2

    print ("el resultado final es:" +str(resultado))

if (operacion == 'b'):
    numero1 = int (input ("Escribe el primer numero"))
    numero2 = int (input ("Escribe el primer numero"))

    resultado = numero1 - numero2

    print ("el resultado final es:" +str(resultado))

if (operacion == 'c'):
    numero1 = int (input ("Escribe el primer numero"))
    numero2 = int (input ("Escribe el primer numero"))

    resultado = numero1 * numero2

    print ("el resultado final es:" +str(resultado))

if (operacion == 'd'):

    try:

        numero1 = int (input ("Escribe el primer numero (No puede ser 0)"))
        numero2 = int (input ("Escribe el primer numero (No puede ser 0)"))

        if numero1 == 0 or numero2 == 0:
            print("No se puede dividir por cero.")
        else:
            resultado = numero1 / numero2
            print ("el resultado final es:" +str(resultado))

    except:

        print("Numeros no válidos")
