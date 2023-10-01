import random

jugadas = 0
v = 0
cp = 0

while jugadas < 5:

    cpu_op = ["piedra", "papel", "tieras"]

    tirada = input("piedra, papel, tijeras, 1,2,3.....")
    cpu = random.choice(cpu_op)

    if (tirada == 'piedra' and cpu == 'tijera'):
        v += 1
        print ("Piedra gana a tijera. ¡VICTORIA! ")

    elif (tirada == 'tijera' and cpu == 'piedra'):
        cp += 1
        print ("Piedra gana a tijera. ¡DERROTA! ")

    elif (tirada == 'papel' and cpu == 'piedra'):
        v += 1
        print ("Papel gana a piedra. ¡VICTORIA! ")

    elif (tirada == 'piedra' and cpu == 'papel'):
        cp += 1
        print ("Papel gana a piedra. ¡DERROTA! ")

    elif (tirada == 'tijera' and cpu == 'papel'):
        v += 1
        print ("Tijeras gana a papel. ¡VICTORIA! ")

    elif (tirada == 'papel' and cpu == 'tijera'):
        cp += 1
        print ("Tijeras gana a papel. ¡DERROTA! ")

    else:
        print ("Los dos habéis hechado los mismo. ¡EMPATE!")

    jugadas += 1

if (cp > v):
    print ("Has perdido:" + str(cp) + "-" + str(v))

elif (v > cp ):
    print ("Has ganado:" + str(v) + "-" + str(cp))

else:
    print ("Habéis empatado" + str(v) + "-" + str(cp))
