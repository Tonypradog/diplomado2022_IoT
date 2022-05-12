
import math


print("\n\n Radio de un circulo inscrito en un triángulo de lados A, B, y C.  \n")

A= float(input("Inserte valor de A: "))
B= float(input("Inserte valor de B: "))
C= float(input("Inserte valor de C: "))

suma=A+B

if (C < suma):
    s=0.5*(A+B+C)
    r=math.sqrt(s*(s-A)*(s-B)*(s-C))/s
    r_rounded = round(r, 2)
    s_rounded = round(s, 2)
    print("S=")
    print(s_rounded)
    print("R=")
    print(r_rounded)
else:
    print("El valor de c no puede ser mayor a la suma de A y B")