import random

def metodo1():

        print("1- Siempre mirando al sol y no soy un caracol. Giro y giro sin fin y no soy un bailarín.")
        sol = input ("a.Girasol, b.Rosa, c.Eucalipto ")

        if(sol == 'a'):
            print("COOORRECTOO!!!\n")
        else:
            print("Respuesta incorrecta")


def metodo2():
        print("2- Tengo agujas pero no sé coser, tengo números pero no sé leer, las horas te doy, ¿Sabes quién soy?")
        sol = input ("a.Maquina coser, b.Taser, c.Reloj ")

        if(sol == 'c'):
            print("COOORRECTOO!!!\n")
        else:
            print("Respuesta incorrecta")


def metodo3():
        print("3- Blanca por dentro, verde por fuera. Si no sabes, espera. ¿Qué es?")
        sol = input ("a.Peladillo, b.Manzana, c.Pera ")

        if(sol == 'c'):
            print("COOORRECTOO!!!\n")
        else:
            print("Respuesta incorrecta")


adiv = [metodo1, metodo2, metodo3]

adi_azar = random.sample(adiv, 1)[0]
adiv.remove(adi_azar)
adi_azar2 = random.sample(adiv, 1)[0]

adi_azar()
adi_azar2()

print ("FIN DEL PROGRAMA DE ADIVINANZAS")



   





