puntuacion = 0

print("1- Siempre mirando al sol y no soy un caracol. Giro y giro sin fin y no soy un bailarín.")
sol = input ("a.Girasol, b.Rosa, c.Eucalipto ")
print("")

if(sol == 'a'):
    print("COOORRECTOO!!!\n")
    puntuacion += 10
else:
    print("Respuesta incorrecta")
    puntuacion -= 10


print("2- Tengo agujas pero no sé coser, tengo números pero no sé leer, las horas te doy, ¿Sabes quién soy?")
sol = input ("a.Maquina coser, b.Taser, c.Reloj ")
print("")

if(sol == 'c'):
    print("COOORRECTOO!!!\n")
    puntuacion += 10
else:
    print("Respuesta incorrecta")
    puntuacion -= 10


print("3- Blanca por dentro, verde por fuera. Si no sabes, espera. ¿Qué es?")
sol = input ("a.Peladillo, b.Manzana, c.Pera ")
print("")

if(sol == 'c'):
    print("COOORRECTOO!!!\n")
    puntuacion += 10
else:
    print("Respuesta incorrecta")
    puntuacion -= 10

print ("Tu puntuacion a sido de :"+str(puntuacion)+"/30")