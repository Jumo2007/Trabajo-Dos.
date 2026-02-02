"""Se coloca un capital C, a un interés I (que oscila entre 0 y 100), durante M años y se desea
saber en cuanto se habrá convertido ese capital en “M” años, sabiendo que es acumulativo.
(Desarrollarlo con un algoritmo iterativo (for, while, etc-)."""

capital = float(input("Ingrese el capital inicial: "))

while capital <= 0:
    print("ERROR: capital inválido")
    capital = float(input("Ingrese el capital inicial: "))

interes = float(input("Ingrese la tasa de interés (0 a 100): "))

while interes < 0 or interes > 100:
    print("ERROR: tasa inválida")
    interes = float(input("Ingrese la tasa de interés (0 a 100): "))

años = int(input("Ingrese la cantidad de años: "))

while años <= 0:
    print("ERROR: cantidad de años inválida")
    años = int(input("Ingrese la cantidad de años: "))

tasa = interes / 100

cont = 0

while cont < años:
    capital += capital * tasa
    cont += 1

print(f"El capital final luego de {años} años es: {capital}")







 

