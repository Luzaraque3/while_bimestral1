# Hallar la suma de los primeros "N" numeros naturales

# input
N = int(input("Didite el valor de N: "))
suma=0
i=1

# processing

while (i<=N):
    suma=suma+i
    i= i +1

print("la suma es: " + str(suma))