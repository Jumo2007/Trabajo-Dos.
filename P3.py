"""Dado que el valor de ex se puede calcular por aproximación de la siguiente suma:

El usuario ingresa x"""

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese la cantidad de términos: "))

suma = 1
factorial = 1
potencia = 1
i = 1

while i <= n:
    potencia *= x
    factorial *= i
    suma += potencia / factorial
    i += 1

print(f"La aproximación de e^{x} es: {suma}")
